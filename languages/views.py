from rest_framework import generics, permissions
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Language
from .serializers import LanguageDetailSerializer, LanguageSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LanguageList(generics.ListCreateAPIView):
    """
    - List out all the languages
    - Option to create new language if logged in
    with owner = request.user
    """
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Language.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__profile',
    ]


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested language
    - Uses the Detail Article serializer to convert language to readonly
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update or delete article info
    """
    serializer_class = LanguageDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Language.objects.all()
