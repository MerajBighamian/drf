from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('title','description','content','slug','author','published_at','status',)
        # exclude = ('created_at')
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        