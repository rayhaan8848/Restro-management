
from django.contrib.auth import get_user_model
from rest_framework import serializers

CustomUser = get_user_model()


class CustomerRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8
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
            "password1",
        ]
        read_only_fields = ["id"]
    def validate(self, data):
        if data['password']!=data['password1']:
            raise serializers.ValidationError("password  and confirm password doesnt matched!!")
        return super().validate(data)

    
    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        validated_data.pop("password1")
        return CustomUser.objects.create_user(
            **validated_data,role='CUSTOMER',is_staff=False,
        is_superuser=False,
        is_active=True,
        )
class AdminRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8
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
            "password1",
        ]
        read_only_fields = ["id"]

    def validate(self, data):
        if data['password']!=data['password1']:
            raise serializers.ValidationError("password  and confirm password doesnt matched!!")
        return super().validate(data)

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        validated_data.pop("password1")
        return CustomUser.objects.create_superuser(
            **validated_data,
        )
    
class StaffRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8
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
            "password1",
        ]
        read_only_fields = ["id"]
     
    def validate(self, data):
        if data['password']!=data['password1']:
            raise serializers.ValidationError("password  and confirm password doesnt matched!!")
        return super().validate(data)

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        
        validated_data.pop("password1")
        validated_data['role'] ='STAFF'
        validated_data['is_staff'] =True
        validated_data['is_superuser']=False
        validated_data['is_active'] =True

        return CustomUser.objects.create_user(
            **validated_data)