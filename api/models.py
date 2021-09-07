from django.db import models
from django.contrib.auth.models import User 
# Django에서 기본적으로 제공하는 User 모델

# Create your models here.

class Post (models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # 외래키 (Django에서 기본 제공하는 User 모델과 M:1 관계)
    title = models.CharField(max_length=144)
    subtitle = models.CharField(max_length=144, blank=True, null=True)
    # blank는 클라이언트가 입력시 공란 가능을 뜻, null은 DB에 입력될때도 null 허용
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '[{}] {}'.format(self.user.username, self.title)