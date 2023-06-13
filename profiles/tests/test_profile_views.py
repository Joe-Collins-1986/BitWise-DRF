from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from profiles.models import Profile

class ProfileListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_list(self):
        '''
        endpoint returns a list of profiles
        '''
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_profile_list_filter_by_profile_name(self):
        '''
        endpoint filters profiles by profile_name
        '''
        response = self.client.get('/profiles/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_profile_list_order_by_article_count(self):
        '''
        endpoint orders profiles by article_count
        '''
        response = self.client.get('/profiles/?ordering=article_count')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for filtering and ordering as desired

class ProfileDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(id=1)

    def test_profile_detail(self):
        '''
        endpoint returns the details of a specific profile
        '''
        profile = Profile.objects.get(id=1)
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        '''
        owner can update a profile
        '''
        self.client.login(username="testuser", password="testpassword")
        data = {'profile_name': 'Updated Profile'}
        response = self.client.put(f'/profiles/{self.profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.profile_name, 'Updated Profile')

    def test_non_owner_update_profile_fail(self):
        '''
        non_owner can NOT update a profile
        '''
        data = {'profile_name': 'Updated Profile'}
        response = self.client.put(f'/profiles/{self.profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.profile_name, 'testuser')