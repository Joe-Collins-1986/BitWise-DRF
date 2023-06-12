from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from languages.models import Language

# from rest_framework.test import APIClient

class LanguageViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.language = Language.objects.create(owner=self.user, language='Python', confidence=80)

    def test_language_list(self):
        """
        Test that language list endpoint returns a list of languages.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get('/languages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual((response.data['count']), 1)

    def test_create_language(self):
        """
        Test that a language can be created by an authenticated user.
        """
        self.client.login(username="testuser", password="testpassword")
        data = {'language': 'JavaScript', 'confidence': 70}
        response = self.client.post('/languages/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Language.objects.count(), 2)

    def test_unauthenticated_user_create_language_fail(self):
        """
        Test that a language cannot be created by an unauthenticated user.
        """
        data = {'language': 'JavaScript', 'confidence': 70}
        response = self.client.post('/languages/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Language.objects.count(), 1)

    def test_language_detail(self):
        """
        Test that language detail endpoint returns the details of a specific language.
        """
        response = self.client.get(f'/languages/{self.language.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_language(self):
        """
        Test that the owner can update a language.
        """
        self.client.login(username="testuser", password="testpassword")
        data = {'language': 'Python', 'confidence': 90}
        response = self.client.put(
            f'/languages/{self.language.id}/',
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.language.refresh_from_db()
        self.assertEqual(self.language.confidence, 90)

    def test_non_owner_update_language_fail(self):
        """
        Test that a non-owner cannot update a language.
        """
        self.client.login(username="testuser2", password="testpassword")
        data = {'language': 'Python', 'confidence': 90}
        response = self.client.put(f'/languages/{self.language.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.language.refresh_from_db()
        self.assertEqual(self.language.confidence, 80)

    def test_delete_language(self):
        """
        Test that the owner can delete a language.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f'/languages/{self.language.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Language.objects.filter(id=self.language.id).exists())

    def test_non_owner_delete_language_fail(self):
        """
        Test that a non-owner cannot delete a language.
        """
        self.client.login(username="testuser2", password="testpassword")
        response = self.client.delete(f'/languages/{self.language.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Language.objects.filter(id=self.language.id).exists())