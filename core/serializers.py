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