from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article
from recommended.models import RecommendedArticle


class RecommendedArticleModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username='testuser1', password='testpass')
        user2 = User.objects.create_user(
            username='testuser2', password='testpass')
        article = Article.objects.create(
            owner=user1,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
        )
        RecommendedArticle.objects.create(
            recommended_by=user1,
            article=article,
            recommended_to=user2
        )

    def test_str_representation(self):
        """
        str provides expected info
        """
        recommendation = RecommendedArticle.objects.get(id=1)
        expected_str = (
            f'Recommended Article: {recommendation.article.article_title}')
        self.assertEqual(str(recommendation), expected_str)

    def test_recommendation_creation(self):
        """
        recommendation is created with the provided data
        """
        recommendation = RecommendedArticle.objects.get(id=1)
        self.assertEqual(recommendation.recommended_by.username, 'testuser1')
        self.assertEqual(recommendation.article.article_title, 'Test Article')
        self.assertEqual(recommendation.recommended_to.username, 'testuser2')
