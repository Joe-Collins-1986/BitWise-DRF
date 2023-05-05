from rest_framework import generics, permissions
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CommentList(generics.ListCreateAPIView):
    """
    - List out all the comments
    - Option to create new comment if logged in
    with owner = request.user
    - Filter to article
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'article',
    ]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested comment
    - Uses Detail Article serializer to convert article to readonly
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update or delete comment info
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()