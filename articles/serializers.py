from rest_framework import serializers

from articles.models import Articles, Comment



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email 
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("article",) 



class ArticleCreateSerializer(serializers.ModelSerializer): # 게시글 작성 하는것도 따로 해줘야함
    class Meta:
        model = Articles
        fields = ("title","content","image")


class ArticleListSerializer(serializers.ModelSerializer): # 필요한 정보만 볼려고함
    user = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField() 
    comment_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    def get_like_count(self, obj): # 좋아요 수 체크
        return obj.like.count()
    
    def get_comment_count(self,obj): # 댓글수 체크
        return obj.comment_set.count()
    
    class Meta:
        model = Articles
        fields = ("id","title","image","updated_at","user","content","like_count","comment_count")

class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ("content",)
