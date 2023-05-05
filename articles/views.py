from rest_framework import generics, permissions, filters
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(generics.ListCreateAPIView):
    """
    - List out all the articles
    - Option to create new aricles if logged in
    with owner = request.user
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested article
    - Uses same Article serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update or delete article info
    """
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all()
