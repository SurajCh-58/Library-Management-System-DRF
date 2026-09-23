from django.contrib import admin
from apps.members.models import Member
# Register your models here.

@admin.action(description="Approve selected member")
def approve_member(modeladmin,request,queryset):
    queryset.filter(status=Member.Status.PENDING).update(status=Member.Status.VERIFIED)

@admin.action(description="Reject selected member")
def reject_member(modeladmin,request,queryset):
    queryset.filter(status=Member.Status.PENDING).update(status=Member.Status.REJECTED)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','status','applied_at']
    list_filter=['status']
    actions=[approve_member,reject_member]