from rest_framework import serializers
from .models import Language
from datetime import date


class LanguageSerializer(serializers.ModelSerializer):
    """
    - Serializer for the Language model
    - Owner shows object owner's username in readonly format
    - Get function to set is_owner to true/false
    - Calculate years experiance form date started using language
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    years_exp = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


def get_years_exp(self, obj):
    if obj.used_since:
        today = date.today()
        years = today.year - obj.used_since.year
        if (today.month < obj.used_since.month or
                (today.month == obj.used_since.month and
                 today.day < obj.used_since.day)):
            years -= 1
        if years < 1:
            return "Less than one year"
        return years
    return "None"

    def validate(self, attrs):
        language = attrs.get('language')
        owner = self.context['request'].user

        if Language.objects.filter(owner=owner, language=language).exists():
            raise serializers.ValidationError(
                {'detail': 'Language already created.'})
        return attrs

    class Meta:
        model = Language
        fields = [
            'id', 'owner', 'language',
            'confidence', 'used_since',
            'is_owner', 'years_exp',
        ]


class LanguageDetailSerializer(LanguageSerializer):
    """
    - Serializer for the Language model - Detailed view
    - Inherits from LanguageSerializer
    - Sets language to readonly
    """
    language = serializers.ReadOnlyField()
