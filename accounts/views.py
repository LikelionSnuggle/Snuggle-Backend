from django.http import JsonResponse
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User, UserInfo
from .serializers import UserInfoSerializer
from rest_framework.authtoken.models import Token


class signupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            infoData = {}
            infoData["Username"] = serializer.data["Username"]
            infoData["birth"] = serializer.data["birth"]
            infoData["tel"] = serializer.data["tel"]
            infoData["email"] = serializer.data["email"]
            infoserializer = UserInfoSerializer(data=infoData)

            if infoserializer.is_valid():
                infoserializer.save()
                print("Userinfo created successfully")
                token = Token.objects.create(user=serializer.instance)
                return Response({"Message": "User created successfully", "token": token.key}, status=201)
            else:
                return Response(infoserializer.errors, status=400)
        return JsonResponse(serializer.data)
        # return Response(UserInfoSerializer.errors, status=400)

# 회원가입은 제대로 되는데, 토큰 발행이 제대로 안됨
# 글고 Username 이 회원가입 완료 시 떴으면 좋겠는데 안뜸..
#
