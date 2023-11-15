from django.urls import path
from .views import CreateListBooksAPIView, RetrieveBookAPIView, CreateListAuthorAPIView, RetrieveAuthorAPIView


urlpatterns = [
    path('book', CreateListBooksAPIView.as_view()),
    path('book/<int:pk>', RetrieveBookAPIView.as_view()),
    path('author', CreateListAuthorAPIView.as_view()),
    path('author/<int:pk>', RetrieveAuthorAPIView.as_view()),
]
