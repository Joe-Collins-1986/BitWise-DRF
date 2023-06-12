from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article


class ArticleModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        Article.objects.create(
            owner=user,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
            github_link='https://github.com/example'
        )

    def test_str_representation(self):
        article = Article.objects.get(id=1)
        expected_str = f'{article.id} {article.article_title}'
        self.assertEqual(str(article), expected_str)