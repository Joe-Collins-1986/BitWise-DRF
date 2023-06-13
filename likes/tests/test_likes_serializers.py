from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from articles.models import Article
from likes.models import Like

class LikeSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='testpassword')
        self.article = Article.objects.create(owner=self.user, article_title='Test Article', article_content='This is a test article.')

    def test_owner_field(self):
        '''
        owner field shows the username of the owner
        '''
        like = Like.objects.create(owner=self.user, article=self.article)
        response = self.client.get(f'/likes/{like.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_create_like(self):
        '''
        Create a new like object
        '''
        data = {
            'article': self.article.id,
        }
        self.client.login(username='user1', password='testpassword')
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_duplicate_like(self):
        '''
        Trying to create a duplicate like object should raise a validation error
        '''
        like = Like.objects.create(owner=self.user, article=self.article)
        data = {
            'article': self.article.id,
        }
        self.client.login(username='user1', password='testpassword')
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, 400)

        error_detail = response.data.get('detail', None)
        self.assertEqual(error_detail, 'Duplication')