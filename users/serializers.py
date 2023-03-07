# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User

# from django.contrib.auth import User
class TinyUserSerializers(ModelSerializer):  # simple user-info
    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "nickname",
            "email",
            "profileImg",
            "pick",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
