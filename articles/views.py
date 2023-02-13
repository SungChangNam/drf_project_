from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer,ArticleListSerializer

# Create your views here.

class ArticleView(APIView):
    def get (self,request):
        article = Article.objects.all()
        serializer = ArticleListSerializer(article,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self,request):
        pass
    
    
class ArticleDetailView(APIView):
    def get (self,request,article_id):
        pass    
    
    def put(self,request,article_id):
        pass
    
    def delete(self,request,article_id):
        pass
    
class CommentView(APIView):
    def get (self,request):
        pass    
    
    def post(self,request):
        pass
    
class CommentDetailView(APIView):
    def put (self,request,comment_id):
        pass    
    
    def delete(self,request,comment_id):
        pass
    
class LikeView(APIView):
    def post (self,request):
        pass    
    
class UnLikeView(APIView):
    def post (self,request):
        pass    
    