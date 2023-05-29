from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Article Model:
    Foreign Key - User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article_title = models.CharField(max_length=255)
    article_content = models.TextField(blank=True)
    primary_language = models.CharField(
        max_length=25,
        blank=True,
    )
    github_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.article_title}'