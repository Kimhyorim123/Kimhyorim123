from django.urls import path
from .views import PostList, PostDetail, CommentsList, CommentsDetail

urlpatterns = [
		#get
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    #댓글 로직 get, post, put, delete
    path('comments/', CommentsList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentsDetail.as_view(), name='comment-detail'),
    
]