from django.shortcuts import render , get_object_or_404
from .models import Article
from django.views.generic import ListView,DetailView
# Create your views here.

class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)
    
class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Article.objects.filter(status=True) , slug=self.kwargs.get('slug'))
