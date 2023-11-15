from django.contrib import admin
from .models import Author, Book, Review


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'biography')
    search_fields = ('name', )
    list_filter = ('name', 'birth_date')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_data', 'price')
    search_fields = ('title', 'publication_data', 'price')
    list_filter = ('title', 'publication_data')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'rating', 'content')
    search_fields = ('reviewer_name', 'rating', 'content')
    list_filter = ('book', 'rating', 'content')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
