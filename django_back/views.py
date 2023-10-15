from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class PerformanceViewSet(viewsets.ModelViewSet):
#     queryset = Performance.objects.all()
#     serializer_class = PerformanceSerializer

# class PageViewSet(viewsets.ModelViewSet):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer

# class PageInfoViewSet(viewsets.ModelViewSet):
#     queryset = PageInfo.objects.all()
#     serializer_class = PageInfoSerializer

# class PageNotificationViewSet(viewsets.ModelViewSet):
#     queryset = PageNotification.objects.all()
#     serializer_class = PageNotificationSerializer

# class PerformanceListViewSet(viewsets.ModelViewSet):
#     queryset = PerformanceList.objects.all()
#     serializer_class = PerformanceListSerializer

# class CalenderViewSet(viewsets.ModelViewSet):
#     queryset = Calender.objects.all()
#     serializer_class = CalenderSerializer
