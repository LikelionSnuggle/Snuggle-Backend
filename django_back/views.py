from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User, Page, Page_intro, Page_notice, Concert, Concert_location, Calender
from .serializers import UserSerializer, PageSerializer, PageIntroSerializer, PageNoticeSerializer, ConcertSerializer, ConcertLocationSerializer, CalenderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageIntroViewSet(viewsets.ModelViewSet):
    queryset = Page_intro.objects.all()
    serializer_class = PageIntroSerializer


class PageNoticeViewSet(viewsets.ModelViewSet):
    queryset = Page_notice.objects.all()
    serializer_class = PageNoticeSerializer


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer


class ConcertLocationViewSet(viewsets.ModelViewSet):
    queryset = Concert_location.objects.all()
    serializer_class = ConcertLocationSerializer


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
