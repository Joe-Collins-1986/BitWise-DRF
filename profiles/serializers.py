from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from recommended.models import RecommendedArticle
from recommended.serializers import ReceivedRecommendationSerializer


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    Get follower id is user is following profile else null
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    received_recommendations = serializers.SerializerMethodField()

    article_count = serializers.ReadOnlyField()
    followed_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    languages_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_received_recommendations(self, obj):
        received_recommendations = RecommendedArticle.objects.filter(
            recommended_to=obj.owner)
        serializer = ReceivedRecommendationSerializer(
            received_recommendations, many=True)
        return serializer.data

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at',
            'profile_name', 'bio', 'image',
            'is_owner', 'following_id',
            'article_count', 'followed_count',
            'following_count', 'languages_count',
            'received_recommendations'
        ]
