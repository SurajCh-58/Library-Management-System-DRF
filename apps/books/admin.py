from django.contrib import admin
from apps.books.models import Category,Author,Book
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name','bio']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','name','category','author']