from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from comments.models import Comment
from likes.models import Like
from followers.models import Follower
from articles.models import Article
from datetime import timedelta
from django.utils import timezone


class ArticleSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            owner=self.user,
            article_title='Test Article',
            article_content='',
            primary_language='',
        )
        self.article.created_at = timezone.now() - timedelta(seconds=35)
        self.article.updated_at = timezone.now()
        self.article.save()

    def test_owner_field(self):
        '''
        owner field shows expected owner
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_is_owner_field_true(self):
        '''
        is_owner field shows true for owner of article
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["is_owner"], True)

    def test_is_owner_field_false(self):
        '''
        is_owner field shows false for non owner of article
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["is_owner"], False)

    def test_get_updated_at_field(self):
        '''
        updated at field calulates correctly between created_at and updated_at
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["updated_at"], "now")

    def test_profile_id_field(self):
        '''
        profile_id shows author profile id
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        expected_profile_id = self.user.profile.id
        self.assertEqual(response.data["profile_id"], expected_profile_id)

    def test_profile_image_field_exists(self):
        '''
        if image exists not none
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertIsNotNone(response.data["profile_image"])

    def test_profile_image_field_none(self):
        '''
        if image does not exist is none
        '''
        self.user.profile.image = None
        self.user.profile.save()
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertIsNone(response.data["profile_image"])

    def test_like_id_field_authenticated_user(self):
        '''
        lkeed_id present if user liked article
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertIsNone(response.data["like_id"])

        like = Like.objects.create(owner=self.user, article=self.article)
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["like_id"], like.id)

    def test_like_id_field_unauthenticated_user(self):
        '''
        if not liked or not logged in liked id is null
        '''
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertIsNone(response.data["like_id"])

    def test_has_user_commented_field_authenticated_user(self):
        '''
        test authenticated user can comment
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertFalse(response.data["has_user_commented"])

        Comment.objects.create(owner=self.user, article=self.article)
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertTrue(response.data["has_user_commented"])

    def test_current_user_comments_count_field_authenticated_user(self):
        '''
        test comment count increases when added
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["current_user_comments_count"], 0)

        Comment.objects.create(owner=self.user, article=self.article)
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.data["current_user_comments_count"], 1)

    def test_is_following_field_authenticated_user(self):
        '''
        test following can be addexd bt authenticated user
        '''
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertFalse(response.data["is_following"])

        Follower.objects.create(owner=self.user, followed=self.user)
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertTrue(response.data["is_following"])
