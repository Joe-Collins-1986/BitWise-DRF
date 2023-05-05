from rest_framework import serializers
from .models import Article
from likes.models import Like

class ArticleSerializer(serializers.ModelSerializer):
    """
    - Serializer for the Article model
    - Owner shows object owner's username in readonly format
    - Get function to set is_owner to true/false
    - Obtain profile id from profile model
    - Obtain profile image form prile model and validate to check it exists
    else return none
    - Get like id if user is liked article else null
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()

    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_profile_image(self, obj):
        profile = obj.owner.profile
        if profile and profile.image:
            return profile.image.url
        return None
    
    def get_like_id(self, obj):
        user=self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, article=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Article
        fields = [
            'id', 'owner', 'created_at',
            'updated_at', 'article_title', 'article_content',
            'primary_language', 'github_link',
            'is_owner', 'profile_id', 'profile_image',
            'like_id', 'comments_count', 'likes_count',
        ]