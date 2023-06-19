from django.db import models
from django.contrib.auth.models import User
from articles.models import Article


class RecommendedArticle(models.Model):
    """
    Recommended Article Model:
    Foreign Key - User (recommended by)
    Foreign Key - Article
    Foreign Key - User (recommended to)
    """
    recommended_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recommendations_given')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    recommended_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_recommendations')

    class Meta:
        unique_together = ['article', 'recommended_to', 'recommended_by']

    def __str__(self):
        return f'Recommended Article: {self.article.article_title}'
