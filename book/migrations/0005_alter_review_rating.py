# Generated by Django 4.2.5 on 2023-11-15 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(max_length=1, validators=[django.core.validators.RegexValidator(message='Rating must be between 1 and 5.', regex='^[1-5]$')]),
        ),
    ]
