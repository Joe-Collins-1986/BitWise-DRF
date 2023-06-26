from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from articles.models import Article
from links.models import Link


class LinkSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            owner=self.user,
            article_title='Test Article',
            article_content='',
            primary_language='',
        )
        self.link = Link.objects.create(
            owner=self.user,
            article=self.article,
            link_title='Test Link',
            link_brief='',
            link_url='https://example.com'
        )

    def test_owner_field(self):
        '''
        owner field shows expected owner
        '''
        response = self.client.get(f'/links/{self.link.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_is_owner_field_true(self):
        '''
        is_owner field shows true for owner of link
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/links/{self.link.id}/')
        self.assertEqual(response.data["is_owner"], True)

    def test_is_owner_field_false(self):
        '''
        is_owner field shows false for non-owner of link
        '''
        User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username="otheruser", password="testpassword")
        response = self.client.get(f'/links/{self.link.id}/')
        self.assertEqual(response.data["is_owner"], False)

    def test_link_title_field(self):
        '''
        link_title field shows expected link title
        '''
        response = self.client.get(f'/links/{self.link.id}/')
        expected_link_title = self.link.link_title
        self.assertEqual(response.data["link_title"], expected_link_title)

    def test_link_brief_field(self):
        '''
        link_brief field shows expected link brief
        '''
        response = self.client.get(f'/links/{self.link.id}/')
        expected_link_brief = self.link.link_brief
        self.assertEqual(response.data["link_brief"], expected_link_brief)

    def test_link_url_field(self):
        '''
        link_url field shows expected link URL
        '''
        response = self.client.get(f'/links/{self.link.id}/')
        expected_link_url = self.link.link_url
        self.assertEqual(response.data["link_url"], expected_link_url)
