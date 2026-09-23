from django.contrib import admin
from apps.borrowings.models import Borrowing
# Register your models here.

@admin.action(description="Update pending status to Borrowed.")
def update_status(ModelAdmin,request,queryset):
    queryset.filter(status=Borrowing.Status.PENDING).update(status=Borrowing.Status.BORROWED)

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display=['id','member','book','borrowed_at','due_date','returned_at','status']
    list_filter=['status']
    actions=[update_status]