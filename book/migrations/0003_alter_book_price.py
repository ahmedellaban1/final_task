# Generated by Django 4.2.5 on 2023-11-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_auther_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
