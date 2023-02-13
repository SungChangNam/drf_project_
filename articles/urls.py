from django.urls import path 
from articles import views


urlpatterns = [
    path("", views.ArticleView.as_view(), name="Article_view"),#게시글 작성
    path("<int:article_id>", views.ArticleDetailView.as_view(), name="Article_detail_view"), #게시글 읽기,수정,삭제
    path("comment/", views.CommentView.as_view(), name="comment_view"),#게시글 댓글
    path("comment/<int:comment_id>", views.CommentDetailView.as_view(), name="comment_detail_view"), #게시글 보기,수정,삭제
    path("like/", views.LikeView.as_view(), name="like_view"), #좋아요
    path("unlike/", views.UnLikeView.as_view(), name="unlike_view"), #싫어요
]
