from django.db import IntegrityError
from rest_framework import serializers
from .models import RecommendedArticle


class ReceivedRecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Received RecommendedArticle model
    Includes the article title and the username of the recommending user
    """

    article_id = serializers.ReadOnlyField(source='article.id')
    article_title = serializers.ReadOnlyField(source='article.article_title')
    recommending_username = serializers.ReadOnlyField(
        source='recommended_by.username')

    class Meta:
        model = RecommendedArticle
        fields = ['id', 'article_id', 'article_title', 'recommending_username']


class RecommendArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for recommending articles
    """

    class Meta:
        model = RecommendedArticle
        fields = ['article', 'recommended_to']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplication'
            })
