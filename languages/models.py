from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Language(models.Model):
    """
    Language Model:
    Foreign Key - User
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="languages")
    language = models.CharField(
        max_length=25,
    )
    confidence = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )
    used_since = models.DateField(null=True)

    class Meta:
        ordering = ['-confidence']

    def __str__(self):
        return f"{self.owner}'s {self.language} experience"
