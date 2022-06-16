from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Categories, Posts, Comment
from .serializers import CategoriesSerializer, PostSerializer, CommentSerializer
# Create your views here.


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.filter(public=True)
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    # /post/{pk}/{url_path}
    @action(methods=['post'], detail=True,
            url_path="hide-post",
            url_name="hide-post")
    def hide_post(self, request, pk):
        try:
            p = Posts.objects.get(pk=pk)
            p.public = False
            p.save()
        except Posts.DoseNotExtis:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=PostSerializer(p).data,
                        status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

