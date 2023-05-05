from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    - Serializer for the Comment model
    - Owner shows users username in readonly format
    - Get function to set is_owner to true/false
    - Obtain profile id from profile model
    - Obtain profile image form profile model and validate to check it exists
    else return none
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_profile_image(self, obj):
        profile = obj.owner.profile
        if profile and profile.image:
            return profile.image.url
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'article',
            'created_at', 'body',
            'is_owner', 'profile_id', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    - Serializer for the Cooment model - Detailed view
    - Inherits from CommentSerializer
    - Sets article to readonly
    """
    article = serializers.ReadOnlyField(source='article.id')
