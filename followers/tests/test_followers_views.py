from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from followers.models import Follower

class FollowerListTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')
        self.user3 = User.objects.create_user(username='user3', password='testpassword')

    def test_follower_list(self):
        '''
        endpoint returns a list of followers
        '''
        Follower.objects.create(owner=self.user1, followed=self.user2)
        Follower.objects.create(owner=self.user1, followed=self.user3)

        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_create_follower_authenticated(self):
        '''
        follower can be created by an authenticated user
        '''
        self.client.login(username='user2', password='testpassword')
        data = {'followed': self.user1.id}
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)

    def test_create_follower_unauthenticated(self):
        '''
        follower creation should fail for an unauthenticated user
        '''
        data = {'followed': self.user1.id}
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Follower.objects.count(), 0)


class FollowerDetailTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')
        self.user3 = User.objects.create_user(username='user3', password='testpassword')
        self.follower = Follower.objects.create(owner=self.user1, followed=self.user2)

    def test_follower_detail(self):
        '''
        endpoint returns the details of a specific follower
        '''
        response = self.client.get(f'/followers/{self.follower.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_follower_owner(self):
        '''
        owner can delete a follower
        '''
        self.client.login(username='user1', password='testpassword')
        response = self.client.delete(f'/followers/{self.follower.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Follower.objects.filter(id=self.follower.id).exists())

    def test_delete_follower_non_owner(self):
        '''
        non-owner should fail to delete a follower
        '''
        self.client.login(username='user3', password='testpassword')
        response = self.client.delete(f'/followers/{self.follower.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Follower.objects.filter(id=self.follower.id).exists())
