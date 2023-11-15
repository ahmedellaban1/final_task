from django.db import models
from django.utils import timezone
from etc.validators import rating_validator

class Author(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    biography = models.TextField(max_length=1000, null=False, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publication_data = models.DateField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=30, null=False, blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)
    rating = models.IntegerField(validators=[rating_validator])

    def __str__(self):
        return self.reviewer_name

