
from django.http import JsonResponse
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response({"Message": "로그인 성공"}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "유효하지 않은 로그인입니다!"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class signupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            infoData = {}
            user = User.objects.get(username=serializer.data["username"])
            infoData["username"] = user.id
            infoData["birth"] = request.data["birth"]
            infoData["tel"] = request.data["tel"]
            infoData["email"] = serializer.data["email"]
            infoserializer = UserInfoSerializer(data=infoData)

            if infoserializer.is_valid():
                infoserializer.save()
                print("Userinfo created successfully")
                token = Token.objects.create(user=User)
                token.save()

                return Response({"Message": "User created successfully", "token": token.key}, status=201)
            else:
                return Response(infoserializer.errors, status=400)
        else:
            return JsonResponse(serializer.data)
            # Response({"Message": "User created successfully", "token": token.key})
            # print(serializer.errors)
            # return Response(serializer.errors, status=400)
