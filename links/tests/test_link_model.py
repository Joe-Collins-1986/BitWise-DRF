from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article
from links.models import Link


class LinkModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testuser', password='testpass')
        article = Article.objects.create(
            owner=user,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
        )
        Link.objects.create(
            owner=user,
            article=article,
            link_title='Test Link',
            link_brief='This is a test link.',
            link_url='https://example.com'
        )

    def test_str_representation(self):
        """
        str provides expected info
        """
        link = Link.objects.get(id=1)
        expected_str = f"{link.owner}'s link for: {link.link_title}"
        self.assertEqual(str(link), expected_str)
