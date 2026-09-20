from django.urls import path
from apps.books.views import BooksListView

urlpatterns = [
    path('/all',BooksListView.as_view(),name="all-books")
]
