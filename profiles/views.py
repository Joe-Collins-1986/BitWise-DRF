from rest_framework import generics
from bitwise.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    - List out all the profiles
    - Profile created by user registration so no create 
    profile required
    - Profiles are not to be deleted unless User is 
    removed so no delete functionality required
    - Due to no create, update, delete no permission class required
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

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
