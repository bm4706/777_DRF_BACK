from django.db import models
from users.models import User

# Create your models here.


class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post/', blank=True)
    created_at = models.DateField(auto_now_add=True) # 생성할때만 추가
    updated_at = models.DateField(auto_now=True) # 세이브할때마다 갱신
    like = models.ManyToManyField(User, related_name="like",blank=True) # 좋아요
    # nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): # admin페이지에서 타이틀해야함
        return str(self.title)
    
    
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 회원id
    article = models.ForeignKey(Articles, on_delete=models.CASCADE) # 게시글번호
    # 글이 삭제되면 글에 작성된 댓글도 사라지게 해야하므로 추가
    content = models.TextField() # 댓글내용
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    
    def __str__(self):
        return str(self.content)