from rest_framework import serializers
from apps.borrowings.models import Borrowing
from rest_framework.validators import UniqueTogetherValidator

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borrowing
        fields=['id','member','book','borrowed_at','due_date','returned_at','status']
        read_only_fields=['borrowed_at','returned_at','status']

        validators=[
            UniqueTogetherValidator(
                queryset=Borrowing.objects.select_related('member','book').all(),
                fields=['member','book'],
                message="Record already exist with same member and book."
            )
        ]

    def validate_member(self,member):
        if member.status != member.Status.VERIFIED:
            raise serializers.ValidationError("only verfied member can borrowed book.")
        return member