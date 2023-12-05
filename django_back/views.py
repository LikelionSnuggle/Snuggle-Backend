from django.http import JsonResponse
from .serializers import UserSerializer
# , UserInfoSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets, status
from rest_framework.views import APIView

from .models import User, Performance, Page, PageInfo, PageNotification, PerformanceList, Calender
from .serializers import UserSerializer, PerformanceSerializer, PageSerializer, PageInfoSerializer, PageNotificationSerializer, PerformanceListSerializer, CalenderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageInfoViewSet(viewsets.ModelViewSet):
    queryset = PageInfo.objects.all()
    serializer_class = PageInfoSerializer


class PageNotificationViewSet(viewsets.ModelViewSet):
    queryset = PageNotification.objects.all()
    serializer_class = PageNotificationSerializer


class PerformanceListViewSet(viewsets.ModelViewSet):
    queryset = PerformanceList.objects.all()
    serializer_class = PerformanceListSerializer


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer


# from django.http import JsonResponse

# Create your views here.


# def signupAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             infoData = {}
#             infoData["user_id"] = serializer.data["id"]
#             infoData["birth"] = serializer.data["birth"]
#             infoData["phone"] = serializer.data["phone"]
#             infoData["email"] = serializer.data["email"]
#             infoserializer = UserInfoSerializer(data=infoData)
#             if infoserializer.is_valid():
#                 infoserializer.save()
#                 print("Userinfo created successfully")
#             else:
#                 return Response(infoserializer.errors, status=400)
#             return Response("Message: User created successfully", status=201)
#         return JsonResponse(serializer.data)
#     return Response(UserInfoSerializer.errors, status=400)

# API key로 인증하는 API 생성
# 추가 예정
