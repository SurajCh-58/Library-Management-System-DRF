from rest_framework.generics import ListAPIView
from apps.books.serializers import BookListSerializer
from apps.books.models import Book

# Create your views here.
class BooksListView(ListAPIView):
    serializer_class=BookListSerializer
    queryset=Book.objects.all()