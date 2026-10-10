
from django.contrib.auth import get_user_model
from rest_framework import serializers

CustomUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8
    )

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "is_active",
            "is_staff",
            "password",
        ]
        read_only_fields = ["id"]

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            **validated_data
        )
