from django.test import TestCase
from django.contrib.auth.models import User
from articles.models import Article
from likes.models import Like


class LikeModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testuser', password='testpass')
        article = Article.objects.create(
            owner=user,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
        )
        Like.objects.create(
            owner=user,
            article=article
        )

    def test_str_representation(self):
        '''
        str provides expected info
        '''
        like = Like.objects.get(id=1)
        expected_str = f"Article: {like.article} by {like.owner}"
        self.assertEqual(str(like), expected_str)

    def test_ordering(self):
        '''
        likes are ordered by created_at in descending order
        '''
        user = User.objects.create_user(
            username='anotheruser', password='testpass')
        article = Article.objects.create(
            owner=user,
            article_title='Article 2',
            article_content='This is another article.',
            primary_language='JavaScript',
        )
        Like.objects.create(
            owner=user,
            article=article
        )

        likes = Like.objects.all()
        self.assertEqual(likes.count(), 2)
        self.assertEqual(likes[0].article.article_title, 'Article 2')
        self.assertEqual(likes[1].article.article_title, 'Test Article')
