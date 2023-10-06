from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from articles.models import Articles
from articles.serializers import ArticleListSerializer, ArticleCreateSerializer
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
