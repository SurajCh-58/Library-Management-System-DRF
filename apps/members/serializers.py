from rest_framework import serializers
from apps.members.models import Member
from apps.common.utils import CaseInsensitiveValidator

class MemberSerializer(serializers.ModelSerializer):
    email=serializers.CharField(
        validators=[
            CaseInsensitiveValidator(
                queryset=Member.objects.all(),
                field_name="email",
                message="Member with this email already exist."
            )
        ]
    )
    class Meta:
        model=Member
        fields=['id','name','email','phone','address','status','applied_at']
        read_only_fields=['id','status','applied_at']