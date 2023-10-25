from django.contrib import admin
from django.urls import path, include

from .views import UserViewSet, PageViewSet, PageIntroViewSet, PageNoticeViewSet, ConcertViewSet, ConcertLocationViewSet, CalenderViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)
routers.register('page', PageViewSet)
routers.register('pageintro', PageIntroViewSet)
routers.register('pagenotice', PageNoticeViewSet)
routers.register('concert', ConcertViewSet)
routers.register('concertlocation', ConcertLocationViewSet)
routers.register('calender', CalenderViewSet)


urlpatterns = [
    path('api/', include(routers.urls)),
]
