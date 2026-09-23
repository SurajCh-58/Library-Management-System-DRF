from django.db import models
from apps.books.models import Book
from apps.members.models import Member
# Create your models here.

class Borrowing(models.Model):
    class Status(models.TextChoices):
        PENDING='pending','Pending'
        BORROWED='brrowed','Brrowed'
        RETURNED='returned','Returned'
        OVERDUE='overdue','Overdue'

    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="borrowings")
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name="borrowings")
    borrowed_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    returned_at=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)

    def __str__(self):
        return f"{self.member} x {self.book}"