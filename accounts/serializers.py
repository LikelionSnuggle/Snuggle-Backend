from .models import UserInfo
from rest_framework import serializers
from django.contrib.auth.models import User
import rest_framework.serializers as serializers
# 회원가입


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
