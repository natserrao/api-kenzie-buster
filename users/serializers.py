from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(
        max_length=127,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message=("email already registered.")
            )
        ],
    )
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    birthdate = serializers.DateField(required=False)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def validate_username(self, username: str) -> str:
        username_already_exists = User.objects.filter(username=username).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already taken.")

        return username


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
