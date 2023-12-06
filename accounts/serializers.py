from .models import UserInfo
from rest_framework import serializers
from django.contrib.auth.models import User
import rest_framework.serializers as serializers
from django.contrib.auth import authenticate
# 회원가입


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# Username and password


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"

# username,email,tel,birth


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
