from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from bitwise.permissions import IsRecipientOrReadOnly
from recommended.serializers import RecommendArticleSerializer, ReceivedRecommendationSerializer
from .models import RecommendedArticle


class ReceivedRecommendationsList(generics.ListAPIView):
    """
    View for retrieving all received recommendations
    Allows the profile owner to view their received recommendations
    """
    serializer_class = ReceivedRecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RecommendedArticle.objects.filter(recommended_to=user)


class RecommendArticle(generics.CreateAPIView):
    """
    View for recommending articles
    Allows authenticated users to recommend articles
    """
    serializer_class = RecommendArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recommended_by=self.request.user)


class DeleteRecommendation(generics.DestroyAPIView):
    """
    View for deleting a recommendation
    Allows the recipient to delete the recommendation
    """
    queryset = RecommendedArticle.objects.all()
    serializer_class = ReceivedRecommendationSerializer
    permission_classes = [IsRecipientOrReadOnly]
