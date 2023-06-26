from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from articles.models import Article
from comments.models import Comment
from datetime import timedelta
from django.utils import timezone


class CommentSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            owner=self.user,
            article_title='Test Article',
            article_content='',
            primary_language='',
        )
        self.comment = Comment.objects.create(
            owner=self.user, article=self.article, body='Test Comment')

        self.comment.created_at = timezone.now() - timedelta(seconds=35)
        self.comment.updated_at = timezone.now()
        self.comment.save()

    def test_owner_field(self):
        '''
        owner field shows expected owner
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_is_owner_field_true(self):
        '''
        is_owner field shows true for owner of comment
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.data["is_owner"], True)

    def test_is_owner_field_false(self):
        '''
        is_owner field shows false for non-owner of comment
        '''
        User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username="otheruser", password="testpassword")
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.data["is_owner"], False)

    def test_profile_id_field(self):
        '''
        profile_id shows author profile id
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        expected_profile_id = self.user.profile.id
        self.assertEqual(response.data["profile_id"], expected_profile_id)

    def test_profile_image_field_exists(self):
        '''
        if image exists, profile_image is not None
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertIsNotNone(response.data["profile_image"])

    def test_profile_image_field_none(self):
        '''
        if image does not exist, profile_image is None
        '''
        self.user.profile.image = None
        self.user.profile.save()
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertIsNone(response.data["profile_image"])

    def test_get_created_at_field(self):
        '''
        created_at field is in naturaltime format
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertIn("ago", response.data["created_at"])

    def test_get_updated_at_field(self):
        '''
        updated_at field is in naturaltime format
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.data["updated_at"], "now")

    def test_get_updated_at_edited_field(self):
        '''
        updated_at_edited field is "Edited"
        if time difference is greater than
        30 seconds, else None
        '''
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.data["updated_at_edited"], "Edited")
