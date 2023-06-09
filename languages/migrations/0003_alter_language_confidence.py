# Generated by Django 3.2.19 on 2023-06-06 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_alter_language_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='confidence',
            field=models.IntegerField(
                blank=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100)]),
        ),
    ]
