from django.test import TestCase
from django.contrib.auth.models import User
from followers.models import Follower


class FollowerModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', password='testpass')
        self.user2 = User.objects.create_user(
            username='user2', password='testpass')
        self.user3 = User.objects.create_user(
            username='user3', password='testpass')

        Follower.objects.create(owner=self.user1, followed=self.user2)
        Follower.objects.create(owner=self.user2, followed=self.user3)
        Follower.objects.create(owner=self.user3, followed=self.user1)

    def test_str_representation(self):
        """
        str provides expected info
        """
        follower = Follower.objects.get(id=1)
        expected_str = f"Owner: {self.user1}, Followed Party: {self.user2}"
        self.assertEqual(str(follower), expected_str)

    def test_ordering(self):
        """
        followers are ordered by created_at in descending order
        """
        followers = Follower.objects.all()
        self.assertEqual(followers.count(), 3)
        self.assertEqual(followers[0].owner, self.user3)
        self.assertEqual(followers[1].owner, self.user2)
        self.assertEqual(followers[2].owner, self.user1)
