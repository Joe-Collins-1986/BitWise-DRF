from django.test import TestCase
from django.contrib.auth.models import User
from comments.models import Comment
from articles.models import Article


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testuser', password='testpass')
        article = Article.objects.create(
            owner=user,
            article_title='Test Article',
            article_content='This is a test article.',
            primary_language='Python',
        )
        Comment.objects.create(
            owner=user,
            article=article,
            body='This is a test comment.'
        )

    def test_str_representation(self):
        '''
        str provides expected info
        '''
        comment = Comment.objects.get(id=1)
        expected_str = comment.body
        self.assertEqual(str(comment), expected_str)

    def test_ordering(self):
        '''
        comments are ordered by created_at in descending order
        '''
        user = User.objects.create_user(
            username='anotheruser', password='testpass')
        article = Article.objects.create(
            owner=user,
            article_title='Another Article',
            article_content='This is another article.',
            primary_language='JavaScript',
        )
        Comment.objects.create(
            owner=user,
            article=article,
            body='This is another comment.'
        )

        comments = Comment.objects.all()
        self.assertEqual(comments.count(), 2)
        self.assertEqual(comments[0].body, 'This is another comment.')
        self.assertEqual(comments[1].body, 'This is a test comment.')
