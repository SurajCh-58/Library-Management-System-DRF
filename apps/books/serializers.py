from rest_framework import serializers
from apps.books.models import Book,Category,Author
from apps.common.utils import CaseInsensitiveValidator

class CategorySerializer(serializers.ModelSerializer):
    name=serializers.CharField(validators=[
    CaseInsensitiveValidator(
        queryset=Category.objects.all(),
        field_name="name",
        message="category with this name already exists."
    )])
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
    name=serializers.CharField(
        validators=[CaseInsensitiveValidator(
            queryset=Book.objects.all(),
            field_name="name",
            message="Book with this name already exists."
          )
        ]
    )   
    class Meta:
        model=Book
        fields=['id','name','category','author']