from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
        

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk','title','image','updated_at','user')