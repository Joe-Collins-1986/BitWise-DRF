# Generated by Django 3.2.19 on 2023-06-21 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_primary_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='github_link',
        ),
    ]