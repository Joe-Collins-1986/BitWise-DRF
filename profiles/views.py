from django.db.models import Count
from rest_framework import generics, filters
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    """
    - List out all the profiles
    - Profile created by user registration so no create 
    profile required
    - Profiles are not to be deleted unless User is 
    removed so no delete functionality required
    - Due to no create, update, delete no permission class required
    - Filter order by counts and date
    - Filer by fieldsets - following, followed, language known
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        article_count = Count('owner__article', distinct=True),
        followed_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        languages_count = Count('owner__languages', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'profile_name',
    ]

    filterset_fields = [
        'owner__following__followed__profile', #LIST OF WHO IS FOLLWONG NAME SELECTED
        'owner__followed__owner__profile', #LIST OF WHO IS FOLLOWED BY NAME SELECTED
        'owner__languages__language'
    ]

    ordering_fields = [
        'article_count',
        'followed_count',
        'following_count',
        'languages_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    - Detail the specificly requested profile
    - Uses same Profile serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update profile info
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
