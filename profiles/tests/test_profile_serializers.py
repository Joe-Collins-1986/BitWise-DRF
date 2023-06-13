from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from followers.models import Follower


class ProfileSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')
        self.profile = Profile.objects.get(id=1)

    def test_owner_field(self):
        """
        owner field shows expected owner's username
        """
        response = self.client.get(f'/profiles/{self.profile.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_is_owner_field_true(self):
        """
        is_owner field shows true for owner of profile
        """
        self.client.login(username="user1", password="testpassword")
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.data["is_owner"], True)

    def test_is_owner_field_false(self):
        """
        is_owner field shows false for non-owner of profile
        """
        self.client.login(username="user2", password="testpassword")
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.data["is_owner"], False)

    def test_following_id_field(self):
        """
        following_id field shows the follower ID if the user is following the profile, else null
        """
        follower = Follower.objects.create(owner=self.user, followed=self.profile.owner)
        self.client.login(username="user1", password="testpassword")
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.data["following_id"], follower.id)

    def test_following_id_field_null(self):
        """
        following_id field is null if the user is not following the profile
        """
        self.client.login(username="user1", password="testpassword")
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertIsNone(response.data["following_id"])
