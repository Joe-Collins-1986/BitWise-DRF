from rest_framework import generics, permissions
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    - List out all the followers
    - Option to create new follower object if logged in
    with owner = request.user
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    - Detail the specificly requested follower
    - Uses same Follower serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can delete follower
    - No need for update, followers works by deleting and
    creating a new follower if required
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
