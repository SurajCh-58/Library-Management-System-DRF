from rest_framework import viewsets
from apps.borrowings.models import Borrowing
from apps.borrowings.serializers import BorrowingSerializer

# Create your views here.
class BorrowingView(viewsets.ModelViewSet):
    serializer_class=BorrowingSerializer

    def get_queryset(self):
        return Borrowing.objects.select_related('member','book').all()