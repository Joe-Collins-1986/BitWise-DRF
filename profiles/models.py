from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    """
    Profile Model:
    1:2:1 Key - User
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    image = ResizedImageField(
        default='../images/profileImages/default-profile-img.jpeg',
        upload_to='images/profileImages/',
        blank=True,
        size=[150, 150],
        crop=['middle', 'center'],
        force_format='JPEG')

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.profile_name:
            self.profile_name = self.owner.username
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
