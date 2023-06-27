from rest_framework import generics, permissions
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Link
from .serializers import LinkSerializer, LinkDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LinkList(generics.ListCreateAPIView):
    """
    - List out all the links
    - Option to create new link if logged in
    with owner = request.user
    """
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Link.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__profile',
        'article',
    ]


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested link
    - Uses the Detail Link serializer to convert article
    and link_title to readonly
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update or delete article info
    """
    serializer_class = LinkDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Link.objects.all()
