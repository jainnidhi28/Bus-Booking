from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from core.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "uuid", "created", "modified"]
        
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Phone number already exists.")
        return value