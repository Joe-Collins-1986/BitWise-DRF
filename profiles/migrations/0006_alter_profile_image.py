# Generated by Django 3.2.19 on 2023-05-16 16:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='..images/profileImages/8CA55562-EF82-4DFA-8D8E-02568B1BFEAD_y2bA6Y5.jpeg', force_format='JPEG', keep_meta=False, quality=90, scale=None, size=[150, 150], upload_to='images/profileImages/'),
        ),
    ]
