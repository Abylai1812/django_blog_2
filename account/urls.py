from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.AccountAPIView.as_view(), name = 'account'),
    path('post/',views.PostAPIView.as_view(), name = 'post'),
]
