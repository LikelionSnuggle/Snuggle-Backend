from django.contrib import admin
from django.urls import path, include

from .views import *
from rest_framework import routers

from django.conf import settings

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)
# routers.register('page', PageViewSet)
routers.register('pageintro', PageIntroViewSet)
routers.register('pagenotice', PageNoticeViewSet)
# routers.register('concert', ConcertViewSet)
routers.register('concertlocation', ConcertLocationViewSet)
routers.register('calender', CalenderViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('page/', PageList.as_view({'get': 'list'})),
    path('page/<int:pk>/', PageDetail.as_view({'get': 'retrieve'})),
    path('concert/', ConcertList.as_view({'get': 'list'})),
    path('concert/<int:pk>/', ConcertDetail.as_view({'get': 'retrieve'})),
]
