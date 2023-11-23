from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import *
from .serializers import *

import haversine


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


class ConcertNear(APIView):
    def get(self, request):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        distance = request.GET.get('distance', 2)  # default 2km
        # print(lat, lon)

        # 근처 distance만큼 이내의 공연장을 모두 불러옴
        concerts = Concert.objects.filter(
            concert_location__lat__range=(
                lat - 0.01 * distance, lat + 0.01 * distance),
            concert_location__lon__range=(
                lon - 0.015 * distance, lon + 0.015 * distance),
        )

        # 거리순으로 정렬
        concerts = sorted(concerts, key=lambda x: haversine.haversine(
            (lat, lon), (x.concert_location.lat, x.concert_location.lon)))

        return Response(ConcertListSerializer(concerts, many=True).data)


class ConcertRecent(APIView):

    def get(self, request):
        # 오늘 날짜 이후
        concerts = Concert.objects.filter(con_time__gte=timezone.now().date())

        concerts = sorted(concerts, key=lambda x: x.con_time)

        return Response(ConcertListSerializer(concerts, many=True).data)


class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
