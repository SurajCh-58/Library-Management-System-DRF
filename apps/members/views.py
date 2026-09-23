from apps.members.serializers import MemberSerializer
from rest_framework.viewsets import ModelViewSet
from apps.members.models import Member



class MemberView(ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer
    http_method_names=['get','post','put','patch','head','option']