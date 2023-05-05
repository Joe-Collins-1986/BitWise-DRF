from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower Model:
    Foreign Key - User X 2
    Create a unique link between owner and followed to stop duplicate follows
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"Owner: {self.owner}, Followed Party: {self.followed}"
