from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/',views.PostAPIView.as_view(), name = 'post'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
