from django.db.models import Count
from rest_framework import generics, permissions, filters
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ArticleList(generics.ListCreateAPIView):
    """
    - List out all the articles
    - Option to create new aricles if logged in
    with owner = request.user
    - Add search filter against article owner and article title
    - Filter order by counts and date of likes and comments
    - Filer by fieldsets - following, followed, article language, profile
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'primary_language',
    ]

    search_fields = [
        'owner__username',
        'article_title',
    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
    ]

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
    queryset = Article.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
