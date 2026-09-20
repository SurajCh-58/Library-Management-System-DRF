from rest_framework import serializers
from apps.books.models import Book,Category,Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name','bio']

class BookListSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    author=serializers.StringRelatedField()   
    class Meta:
        model=Book
        fields=['id','name','category','author']