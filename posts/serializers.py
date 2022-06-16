from rest_framework.serializers import ModelSerializer
from .models import *


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['categories_id', 'categories_name']


class PostSerializer(ModelSerializer):
    categories = CategoriesSerializer()

    class Meta:
        model = Posts
        fields = ['id', 'categories', 'title', 'content', 'time', 'public', 'image']


class CommentSerializer(ModelSerializer):
    posts_id = PostSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'posts_id', 'comment_user', 'comment_content', 'time']
