from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from blog.models import Post
from serializers import PostListSerializers, PostCreateSerializer
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

# class AccountAPIView(APIView):
    
#     def get(self, request):
#         accounts_mobile_phones  = UserAccount.objects.all().values('mobile_phone')
#         return Response(list(accounts_mobile_phones))
    
#     def post(self,request):
#         print(request.data)
#         return Response('test')
    
# class PostAPIView(APIView):
    
#     def get(self, request):
#         post_queryset = Post.objects.all()
#         serializer = PostListSerializers(post_queryset, many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = PostCreateSerializer(data = request.data)
#         serializer.is_valid()
#         user = User.objects.get(id = serializer.validated_data.pop(user))
#         categories = serializer.validated_data.pop('categories')
#         post = Post.objects.create(user = user,**serializer.validated_data)
#         post.categories.add(*categories)
        
#         return Response("Created!")
    
#     def delete(self, request, pk, format = None):
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)


class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCreateSerializer
    
    def create_view(self, serializer):
        user = self.request.user 
        categories = serializer.validated_data.pop('categories')
        post = serializer.save(user=user)
        post.categories.add(*categories)

class PostDetailAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializers

    def delete(self, request):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)