from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from articles.models import Article
from likes.models import Like

class LikeListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.article = Article.objects.create(article_title='Test Article', owner=self.user)
        self.article2 = Article.objects.create(article_title='Test Article 2', owner=self.user)
        self.like = Like.objects.create(article=self.article, owner=self.user)

    def test_like_list(self):
        '''
        endpoint returns a list of likes
        '''
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_like_authenticated_user(self):
        '''
        like can be created by an authenticated user
        '''
        self.client.login(username='testuser', password='testpassword')
        data = {'article': self.article2.id}
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 2)

    def test_create_like_unauthenticated_user_fail(self):
        '''
        like creation forbidden for unauthenticated user
        '''
        data = {'article': self.article.id}
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 1)

class LikeDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(article_title='Test Article', owner=self.user)
        self.like = Like.objects.create(article=self.article, owner=self.user)

    def test_like_detail(self):
        '''
        endpoint returns the details of a specific like
        '''
        response = self.client.get(f'/likes/{self.like.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_like_owner(self):
        '''
        owner can delete a like
        '''
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(f'/likes/{self.like.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Like.objects.filter(id=self.like.id).exists())

    def test_non_owner_delete_like_fail(self):
        '''
        non-owner can NOT delete a like
        '''
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.delete(f'/likes/{self.like.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Like.objects.filter(id=self.like.id).exists())