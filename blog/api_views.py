from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]