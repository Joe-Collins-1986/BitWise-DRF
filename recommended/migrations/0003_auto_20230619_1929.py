# Generated by Django 3.2.19 on 2023-06-19 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommended', '0002_alter_recommendedarticle_recommended_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendedarticle',
            name='recommended_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations_given', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recommendedarticle',
            name='recommended_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_recommendations', to=settings.AUTH_USER_MODEL),
        ),
    ]
