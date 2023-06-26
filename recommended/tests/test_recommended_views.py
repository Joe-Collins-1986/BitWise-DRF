from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from recommended.models import RecommendedArticle
from articles.models import Article


class ReceivedRecommendationsListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        self.user2 = User.objects.create_user(
            username='testuser2', password='testpassword')

        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)
        self.article2 = Article.objects.create(
            article_title='Test Article 2', owner=self.user)

        self.recommendation = RecommendedArticle.objects.create(
            recommended_by=self.user, article=self.article, recommended_to=self.user)
        self.recommendation2 = RecommendedArticle.objects.create(
            recommended_by=self.user, article=self.article2, recommended_to=self.user)

    def test_received_recommendations_list(self):
        """
        endpoint returns a list of received recommendations for the authenticated user
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get('/recomendations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(
            response.data['results'][0]['recommending_username'], self.user.username)

    def test_safe_recommendations_list(self):
        """
        if logged in but recipient of none return no results
        """
        self.client.login(username="testuser2", password="testpassword")
        response = self.client.get('/recomendations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_received_recommendations_list_unauthenticated(self):
        """
        endpoint returns a 403 error when accessed by an unauthenticated user
        """
        response = self.client.get('/recomendations/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecommendArticleTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(
            username='testuser2', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)

        self.recommendation = RecommendedArticle.objects.create(
            recommended_by=self.user, article=self.article, recommended_to=self.user2)

    def test_recommend_article(self):
        """
        authenticated user can recommend an article
        """
        self.client.login(username="testuser", password="testpassword")
        data = {'article': self.article.id, 'recommended_to': self.user.id}
        response = self.client.post('/recomendations/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_recommend_article_unauthenticated(self):
        """
        endpoint returns a 403 error when accessed by an unauthenticated user
        """
        data = {'article': self.article.id, 'recommended_to': self.user2.id}
        response = self.client.post('/recomendations/add/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_recommendation(self):
        """
        recipient can delete a recommendation
        """
        self.client.login(username="testuser2", password="testpassword")
        response = self.client.delete(
            f'/recomendations/remove/{self.recommendation.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(RecommendedArticle.objects.filter(
            id=self.recommendation.id).exists())

    def test_delete_recommendation_non_recipient_fail(self):
        """
        non-recipient can NOT delete a recommendation
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(
            f'/recomendations/remove/{self.recommendation.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(RecommendedArticle.objects.filter(
            id=self.recommendation.id).exists())
