from django.db import models
from django.contrib.auth.models import User
from articles.models import Article


class Link(models.Model):
    """
    Link Model:
    Foreign Key - User
    """
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="links_owner")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="links_article")

    link_title = models.CharField(max_length=255)
    link_brief = models.TextField(blank=True)
    link_url = models.URLField(max_length=255)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s link for: {self.link_title}"
