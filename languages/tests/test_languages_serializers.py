from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from languages.models import Language
from datetime import date
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

class LanguageSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')
        self.language = Language.objects.create(
            owner=self.user,
            language='Python',
            confidence= 90,
            used_since=date(2015, 1, 1),
        )
        self.language2 = Language.objects.create(
            owner=self.user,
            language='JavaScript',
            confidence= 50,
            )
        self.language3 = Language.objects.create(
            owner=self.user,
            language='JavaScript',
            confidence= 50,
            used_since=timezone.now(),
            )
        self.language4 = Language.objects.create(
            owner=self.user,
            language='JavaScript',
            confidence= 50,
            used_since=timezone.now()- timedelta(days=19 * 31),
            )
    


    def test_owner_field(self):
        """
        owner field shows expected owner
        """

        response = self.client.get(f'/languages/{self.language.id}/')
        expected_owner = self.user.username
        self.assertEqual(response.data["owner"], expected_owner)

    def test_is_owner_field_true(self):
        """
        is_owner field shows true for owner of language
        """
        self.client.login(username="user1", password="testpassword")
        response = self.client.get(f'/languages/{self.language.id}/')
        self.assertEqual(response.data["is_owner"], True)

    def test_is_owner_field_false(self):
        """
        is_owner field shows false for non-owner of language
        """
        self.client.login(username="user2", password="testpassword")
        response = self.client.get(f'/languages/{self.language.id}/')
        self.assertEqual(response.data["is_owner"], False)

    def test_years_exp_field(self):
        """
        years_exp field shows correct years of experience
        """
        response = self.client.get(f'/languages/{self.language.id}/')
        expected_years_exp = 8 
        self.assertEqual(response.data["years_exp"], expected_years_exp)

    def test_less_than_one_years_exp_field(self):
        """
        years_exp field shows less than one
        """
        response = self.client.get(f'/languages/{self.language3.id}/')
        expected_years_exp = 'Less than one year'
        self.assertEqual(response.data["years_exp"], expected_years_exp)

    def test_between_one_and_two_years_exp_field(self):
        """
        years_exp field shows one
        """
        response = self.client.get(f'/languages/{self.language4.id}/')
        expected_years_exp = 1
        self.assertEqual(response.data["years_exp"], expected_years_exp)

    def test_years_exp_field_none(self):
        """
        years_exp field is 'None' if used_since is not provided
        """
        response = self.client.get(f'/languages/{self.language2.id}/')
        self.assertEqual(response.data["years_exp"], "None")

    def test_language_already_created(self):
        """
        Language creation is not allowed if it already exists for the owner
        """
        self.client.login(username="user1", password="testpassword")
        data = {
            'language': 'Python',
            'confidence': 60,
            'used_since': date(2010, 1, 1)
        }
        response = self.client.post(f'/languages/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_detail = response.data.get('detail', None)
        self.assertEqual(error_detail[0], 'Language already created.')

    def test_language_creation(self):
        """
        Language creation is successful if all fields are provided correctly
        """
        self.client.login(username="user1", password="testpassword")
        data = {
            'language': 'Java',
            'confidence': 20,
            'used_since': date(2019, 1, 1)
        }
        response = self.client.post(f'/languages/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Language.objects.count(), 5)
        self.assertEqual(response.data['owner'], self.user.username)
        self.assertEqual(response.data['language'], 'Java')
        self.assertEqual(response.data['confidence'], 20)
        self.assertEqual(response.data['used_since'], '2019-01-01')