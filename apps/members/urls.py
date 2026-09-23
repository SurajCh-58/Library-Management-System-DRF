from django.urls import path,include
from apps.members.views import MemberView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'member',MemberView,basename='member')

urlpatterns = [
    path('',include(router.urls))
]
