from django.db import models

# Create your models here.
class Member(models.Model):
    class Status(models.TextChoices):
        PENDING='pending','Pending'
        VERIFIED='verified','Verfied'
        REJECTED='rejected','Rejected'
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField()
    address=models.TextField()
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    applied_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name