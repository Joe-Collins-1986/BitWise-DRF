from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article


class ArticleModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testuser', password='testpass')
        Article.objects.create(
            owner=user,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
        )

    def test_str_representation(self):
        '''
        str provides expected info
        '''
        article = Article.objects.get(id=1)
        expected_str = f'{article.id} {article.article_title}'
        self.assertEqual(str(article), expected_str)

    def test_ordering(self):
        '''
        articles are ordered by created_at in descending order
        '''
        user = User.objects.create_user(
            username='anotheruser', password='testpass')
        article1 = Article.objects.create(
            owner=user,
            article_title='Article 1',
            article_content='This is article 1.',
            primary_language='Python',
        )
        article2 = Article.objects.create(
            owner=user,
            article_title='Article 2',
            article_content='This is article 2.',
            primary_language='Python',
        )

        articles = Article.objects.all()
        self.assertEqual(articles.count(), 3)
        self.assertEqual(articles[0], article2)
        self.assertEqual(articles[1], article1)
        self.assertEqual(articles[2].article_title, 'Test Article')
