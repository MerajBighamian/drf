from django.urls import path
from .views import ArticleView,ArticleDetail , UserDetail , UserList

app_name = 'api'

urlpatterns = [
    path('',ArticleView.as_view(),name='list'),
    path('<slug:slug>',ArticleDetail.as_view(),name='detail'),
    path('users/',UserList.as_view(),name='user-list'),
    path('users/<int:pk>',UserDetail.as_view(),name='user-detail'),

]
