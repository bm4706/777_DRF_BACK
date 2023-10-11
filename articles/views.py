from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from articles.models import Articles, Comment
from articles.serializers import ArticleListSerializer, ArticleCreateSerializer, CommentCreateSerializer, CommentSerializer
from rest_framework.generics import get_object_or_404

# 
class ArticleView(APIView):
    def get(self, request): # 게시글 요청
        # print("get요청입니다.")
        articles = Articles.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
    def post(self, request): # 게시글 작성
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # print("post요청입니다.")
        
        
class ArticleDetailView(APIView):
    def get(self,request, article_id):
        article = get_object_or_404(Articles, id=article_id)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # print("get요청")
        
    def put(self,request, article_id):
        article = get_object_or_404(Articles, id=article_id)
        if request.user == article.user: # 수정은 게시글 작성만이 가능하게 해야하므로
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)
        # print("put요청")
        
    def delete(self,request, article_id):
        article = get_object_or_404(Articles, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response("삭제완료", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)
        # print("delete요청")
        

class CommentView(APIView):
    def get(self, request, article_id):
        article = Articles.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # print("get요청")
    def post(self, request, article_id): # 댓글 생성 기능
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id )
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # print("post요청") 

        
class CommentDetailView(APIView):
    def put(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN) 
            
            
        # print("put 요청")
        
    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("삭제완료",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이없습니다.", status=status.HTTP_403_FORBIDDEN)
        # print("delete요청")
       
    
class Like_View(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Articles, id=article_id) # 게시글 id 불러오는 변수
        if request.user != article.user:
            if request.user in article.like.all(): # 좋아요 취소
                article.like.remove(request.user)
                return Response("좋아요 취소!", status=status.HTTP_200_OK)
            else: # 좋아요
                article.like.add(request.user)
                return Response("좋아요", status=status.HTTP_200_OK)
        else:
            return Response("자추금지.", status=status.HTTP_406_NOT_ACCEPTABLE)