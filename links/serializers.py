from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    """
    - Serializer for the Liknk model
    - Owner shows object owner's username in readonly format
    - Article shows object tile in readonly format
    - Get function to set is_owner to true/false
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Link
        fields = [
            'id', 'owner', 'is_owner',
            'article', 'link_title',
            'link_brief', 'link_url',
        ]


class LinkDetailSerializer(LinkSerializer):
    """
    - Serializer for the Link model - Detailed view
    - Inherits from LinkSerializer
    - Sets link_title to readonly
    """
    article = serializers.ReadOnlyField()
    link_title = serializers.ReadOnlyField()
