from django.shortcuts import render
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer, Author, Book, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status


class CreateListBooksAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_data', 'price', ]
    search_fields = ['title', 'author']
    ordering_fields = ['id', 'publication_data', 'price']


class RetrieveBookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'pk'
    serializer_class = BookSerializer

    def get(self, request, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['pk'])
        except Author.DoesNotExist:
            return Response({"message": 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        book_serializer = BookSerializer(book)
        reviews = Review.objects.filter(book=book)
        reviews_serializer = ReviewSerializer(reviews, many=True)
        return Response({
            'book': book_serializer.data,
            'reviews': reviews_serializer.data,
        }, status=status.HTTP_200_OK)

class CreateListAuthorAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'birth_date', 'biography', ]
    search_fields = ['name', 'birth_date']
    ordering_fields = ['id', 'name']


class RetrieveAuthorAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    lookup_field = 'pk'
    serializer_class = AuthorSerializer

    def get(self, request, **kwargs):
        try:
            author = Author.objects.get(id=kwargs['pk'])
        except Author.DoesNotExist:
            return Response({"message": 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
        author_serializer = AuthorSerializer(author)
        books = Book.objects.filter(author=author)
        book_serializer = BookSerializer(books, many=True)
        return Response({
            'author': author_serializer.data,
            'books': book_serializer.data,
        }, status=status.HTTP_200_OK)
