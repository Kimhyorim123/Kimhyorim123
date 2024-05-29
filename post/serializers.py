from rest_framework.serializers import ModelSerializer
from .models import Post
from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'createAt', 'updateAt']

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'