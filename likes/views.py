from rest_framework import generics, permissions
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    - List out all the likes
    - Option to create like if logged in
    with owner = request.user
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    - Detail the specificly requested like
    - Uses same Like serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can delete article info
    - No need for update, likes works of deleting and
    creating a new like if required
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
