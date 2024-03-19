from rest_framework import serializers
from blog.models import Post
from .models import User
# class PostListSerializers(serializers.Serializer):
#     title = serializers.CharField()
#     is_active = serializers.BooleanField()
    
# class PostCreateSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_active = serializers.BooleanField()
#     user = serializers.IntegerFieldField()
#     categories = serializers.ListField()

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'is_active']
        read_only_fields = ['id']

class PostCreateSerializer(serializers.ModelSerializer):
    categories = serializers.ListField()

    class Meta:
        model = Post
        fields = ['title', 'is_active', 'user', 'categories']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
