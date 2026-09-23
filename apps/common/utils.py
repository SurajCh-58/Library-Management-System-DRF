from rest_framework import serializers

class CaseInsensitiveValidator:
    requires_context=True
    def __init__(self,queryset,field_name,message=None):
        self.queryset=queryset
        self.field_name=field_name
        self.message=message or 'This value already exists.'

    def __call__(self,value,serailizer_field):
        instance=getattr(serailizer_field.parent,'instance',None)

        queryset=self.queryset.filter(**{f"{self.field_name}__iexact":value})

        if instance is not None:
            queryset=queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(self.message)
        return value