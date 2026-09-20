from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="categories"
        ordering=["id"]

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['id']
         
class Book(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="book_author")

    def __str__(self):
        return self.name
    class Meta:
        ordering=['id']