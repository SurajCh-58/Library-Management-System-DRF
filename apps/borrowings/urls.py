from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.borrowings.views import BorrowingView

router=DefaultRouter()
router.register(r"borrowing",BorrowingView,basename='borrowings')

urlpatterns = [
    path('',include(router.urls))
]
