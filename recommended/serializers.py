from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import RecommendedArticle


class ReceivedRecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Received RecommendedArticle model
    Includes the article title and the username of the recommending user
    """

    article_id = serializers.ReadOnlyField(source='article.id')
    article_title = serializers.ReadOnlyField(source='article.article_title')
    recommending_id = serializers.ReadOnlyField(
        source='recommended_by.id')
    recommending_username = serializers.ReadOnlyField(
        source='recommended_by.username')
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = RecommendedArticle
        fields = ['id', 'article_id', 'article_title',
                  'recommending_id', 'recommending_username',
                  'created_at']


class RecommendArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for recommending articles
    """

    class Meta:
        model = RecommendedArticle
        fields = ['article', 'recommended_to']
