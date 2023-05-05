from django.db import IntegrityError
from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    - Serializer for the Like model
    - Owner shows users username in readonly format
    - Get function to set is_owner to true/false
    - Validate if like already exists between user and 
    article and present tailored error message if duplication 
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'article',
            'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplication'
            })