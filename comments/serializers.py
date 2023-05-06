from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from datetime import timedelta

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

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    updated_at_edited = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def get_updated_at_edited(self, obj):
        time_diff = obj.updated_at - obj.created_at
        if time_diff <= timedelta(seconds=30):
            return None
        return "Edited"
    
    def get_profile_image(self, obj):
        profile = obj.owner.profile
        if profile and profile.image:
            return profile.image.url
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'article',
            'created_at', 'updated_at', 'updated_at_edited', 'body',
            'is_owner', 'profile_id', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    - Serializer for the Cooment model - Detailed view
    - Inherits from CommentSerializer
    - Sets article to readonly
    """
    article = serializers.ReadOnlyField(source='article.id')
