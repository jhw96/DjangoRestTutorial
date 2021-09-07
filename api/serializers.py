# api/serializers
'''
serializer는 queryset과 파이썬객체,모델 인스턴스와 같은 
복잡한 데이터를 JSON, XML 등으로 쉽게 변환할 수 있다.

쿼리셋 : 데이터베이스에서 전달받은 모델의 객체 목록
'''
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'created_at'
        )
        read_only_fields = ('created_at',)
