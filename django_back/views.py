from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PageDetail(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer


class PageList(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer


class PageIntroViewSet(viewsets.ModelViewSet):
    queryset = Page_intro.objects.all()
    serializer_class = PageIntroSerializer


class PageNoticeViewSet(viewsets.ModelViewSet):
    queryset = Page_notice.objects.all()
    serializer_class = PageNoticeSerializer


class ConcertDetail(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertDetailSerializer


class ConcertList(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertListSerializer


class ConcertLocationViewSet(viewsets.ModelViewSet):
    queryset = Concert_location.objects.all()
    serializer_class = ConcertLocationSerializer


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
