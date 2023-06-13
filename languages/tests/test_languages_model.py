from django.test import TestCase
from django.contrib.auth.models import User
from languages.models import Language


class LanguageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        Language.objects.create(
            owner=self.user,
            language='Python',
            confidence=80,
            used_since='2022-01-01'
        )
        Language.objects.create(
            owner=self.user,
            language='JavaScript',
            confidence=90,
            used_since='2021-05-01'
        )

    def test_str_representation(self):
        """
        str provides expected info
        """
        language = Language.objects.get(id=1)
        expected_str = f"{self.user}'s {language.language} experience"
        self.assertEqual(str(language), expected_str)

    def test_ordering(self):
        """
        languages are ordered by confidence in descending order
        """
        Language.objects.create(
            owner=self.user,
            language='Java',
            confidence=70,
            used_since='2020-10-01'
        )

        languages = Language.objects.all()
        self.assertEqual(languages.count(), 3)
        self.assertEqual(languages[0].language, 'JavaScript')
        self.assertEqual(languages[1].language, 'Python')
        self.assertEqual(languages[2].language, 'Java')
