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


# 로그인부분 시리얼라이저 - 코드 작성중입니다 ㅜㅜ !!
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found'
            )
