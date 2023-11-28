
from django.http import JsonResponse
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User, UserInfo
from .serializers import UserInfoSerializer


class signupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            infoData = {}
            infoData["user_id"] = serializer.data["id"]
            infoData["birth"] = serializer.data["birth"]
            infoData["phone"] = serializer.data["phone"]
            infoData["email"] = serializer.data["email"]
            infoserializer = UserInfoSerializer(data=infoData)
            if infoserializer.is_valid():
                infoserializer.save()
                print("Userinfo created successfully")
            else:
                return Response(infoserializer.errors, status=400)
            return Response("Message: User created successfully", status=201)
        return JsonResponse(serializer.data)
        # return Response(UserInfoSerializer.errors, status=400)
