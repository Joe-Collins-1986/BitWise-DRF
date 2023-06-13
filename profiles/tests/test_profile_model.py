from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass')

    def test_str_representation(self):
        '''
        str provides expected info
        '''
        profile = Profile.objects.get(id=1)
        expected_str = f"{profile.owner}'s profile"
        self.assertEqual(str(profile), expected_str)

    def test_profile_name_set_to_username(self):
        '''
        profile_name is set to username if not provided
        '''
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.profile_name, 'testuser')

    def test_ordering(self):
        '''
        profiles are ordered by created_at in descending order
        '''

        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 2)
        self.assertEqual(profiles[0].owner, self.user2)
        self.assertEqual(profiles[1].owner, self.user)

