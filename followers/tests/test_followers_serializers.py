from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from followers.models import Follower


class FollowerSerializerTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', password='testpassword')
        self.user2 = User.objects.create_user(
            username='user2', password='testpassword')
        self.user3 = User.objects.create_user(
            username='user3', password='testpassword')

        self.follower = Follower.objects.create(
            owner=self.user1, followed=self.user2)

    def test_owner_field(self):
        '''
        owner field shows the username of the owner
        '''
        response = self.client.get(f'/followers/{self.follower.id}/')
        expected_owner = self.user1.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_followed_name_field(self):
        '''
        followed_name field shows the username of the followed user
        '''
        response = self.client.get(f'/followers/{self.follower.id}/')
        expected_followed_name = self.user2.username
        self.assertEqual(
            response.data["followed_name"],
            expected_followed_name)

    def test_create_follower(self):
        '''
        Create a new follower object
        '''
        data = {
            'followed': self.user3.id,
        }
        self.client.login(username='user1', password='testpassword')
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, 201)

    def test_create_duplicate_follower(self):
        """
        Trying to create a duplicate follower object
        should raise a validation error
        """
        self.client.login(username='user1', password='testpassword')
        data = {
            'followed': self.user2.id,
        }
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, 400)

        error_detail = response.data.get('detail', None)
        self.assertEqual(error_detail, 'Duplication')
