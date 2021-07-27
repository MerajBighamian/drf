from django.shortcuts import render
from blog.models import Article
from .serializer import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser
# Create your views here.

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)