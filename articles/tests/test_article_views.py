from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)

    def test_article_list(self):
        '''
        endpoint returns a list of articles
        '''
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual((response.data['count']), 1)

    def test_create_article(self):
        '''
        article can be created by an authenticated user
        '''
        data = {'article_title': 'New Article'}
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post('/articles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 2)

    def test_unauthenticated_user_create_article_fail(self):
        '''
        article can NOT be created by an un-authenticated user
        '''
        data = {'article_title': 'New Article'}
        response = self.client.post('/articles/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Article.objects.count(), 1)


class ArticleDetailTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)

    def test_article_detail(self):
        '''
        endpoint returns the details of a specific article
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        '''
        owner can update an article
        '''
        self.client.login(username="testuser", password="testpassword")
        data = {'article_title': 'Updated Article'}
        response = self.client.put(f'/articles/{self.article.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.article.refresh_from_db()
        self.assertEqual(self.article.article_title, 'Updated Article')

    def test_non_owner_update_article_fail(self):
        '''
        non_owner can NOT update an article
        '''
        data = {'article_title': 'Updated Article'}
        response = self.client.put(f'/articles/{self.article.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.article.refresh_from_db()
        self.assertEqual(self.article.article_title, 'Test Article')

    def test_delete_article(self):
        '''
        owner can delete an article
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f'/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())

    def test_non_owner_delete_article_fail(self):
        '''
        non_owner can NOT delete an article
        '''
        response = self.client.delete(f'/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Article.objects.filter(id=self.article.id).exists())
