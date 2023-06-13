from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from comments.models import Comment
from articles.models import Article


class CommentListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)
        self.comment = Comment.objects.create(
            article=self.article, owner=self.user, body='Test Comment')

    def test_comment_list(self):
        '''
        endpoint returns a list of comments
        '''
        response = self.client.get(f'/comments/?article={self.article.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_comment(self):
        '''
        comment can be created by an authenticated user
        '''
        data = {'article': self.article.id, 'body': 'New Comment'}
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_unauthenticated_user_create_comment_fail(self):
        '''
        comment can NOT be created by an un-authenticated user
        '''
        data = {'article': self.article.id, 'body': 'New Comment'}
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.count(), 1)


class CommentDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            article_title='Test Article', owner=self.user)
        self.comment = Comment.objects.create(
            article=self.article, owner=self.user, body='Test Comment')

    def test_comment_detail(self):
        '''
        endpoint returns the details of a specific comment
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        '''
        owner can update a comment
        '''
        self.client.login(username="testuser", password="testpassword")
        data = {'body': 'Updated Comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Updated Comment')

    def test_non_owner_update_comment_fail(self):
        '''
        non_owner can NOT update a comment
        '''
        data = {'body': 'Updated Comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, 'Test Comment')

    def test_delete_comment(self):
        '''
        owner can delete a comment
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_non_owner_delete_comment_fail(self):
        '''
        non_owner can NOT delete a comment
        '''
        response = self.client.delete(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Comment.objects.filter(id=self.comment.id).exists())
