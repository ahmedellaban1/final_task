import random, os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from faker import Faker
from book.models import Author, Book, Review


fake = Faker()
def create_author(n):
    for _ in range(n):
        Author.objects.create(
            name=fake.name(),
            birth_date=fake.date(),
            biography=fake.text()
        )


def create_book(n):
    integer_values = [i + 130 for i in range(1000)]
    author = Author.objects.all().order_by('?')
    for _ in range(n):
        Book.objects.create(
            title=fake.name(),
            author=author[random.randint(1, 99)],
            publication_data=fake.date(),
            price=integer_values[random.randint(1, len(integer_values)-1)]
        )


def create_review(n):
    book = Book.objects.all().order_by('?')
    for _ in range(n):
        Review.objects.create(
            book=book[random.randint(1, 1999)],
            reviewer_name=fake.name(),
            content=fake.text(),
            rating=random.randint(1, 5)
        )


# create_author(100)
#
#
# create_book(2000)


create_review(2000)
