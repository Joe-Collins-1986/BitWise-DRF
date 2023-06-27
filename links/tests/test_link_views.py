from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from links.models import Link
from articles.models import Article


class LinkListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)
        self.link = Link.objects.create(
            link_title='Test Link',
            link_url='https://example.com',
            article=self.article, owner=self.user)

    def test_link_list(self):
        """
        Endpoint returns a list of links.
        """
        response = self.client.get('/links/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_link(self):
        """
        Link can be created by an authenticated user.
        """
        data = {'link_title': 'New Link',
                'link_url': 'https://example.com', 'article': self.article.id}
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post('/links/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Link.objects.count(), 2)

    def test_unauthenticated_user_create_link_fail(self):
        """
        Link can NOT be created by an unauthenticated user.
        """
        data = {'link_title': 'New Link',
                'link_url': 'https://example.com', 'article': self.article.id}
        response = self.client.post('/links/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Link.objects.count(), 1)


class LinkDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article',
            owner=self.user)
        self.link = Link.objects.create(
            link_title='Test Link',
            link_url='https://example.com',
            article=self.article, owner=self.user)

    def test_delete_link(self):
        """
        Owner can delete a link.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f'/links/{self.link.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Link.objects.filter(id=self.link.id).exists())

    def test_non_owner_update_link_fail(self):
        """
        Non-owner can NOT update a link.
        """
        data = {'link_url': 'https://new.com', 'article': self.article.id}
        response = self.client.put(f'/links/{self.link.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.link.refresh_from_db()
        self.assertEqual(self.link.link_title, 'Test Link')

    def test_non_owner_delete_link_fail(self):
        """
        Non-owner can NOT delete a link.
        """
        response = self.client.delete(f'/links/{self.link.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Link.objects.filter(id=self.link.id).exists())
