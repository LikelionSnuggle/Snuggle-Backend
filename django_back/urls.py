from django.urls import include
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
# routers.register('calender', CalenderViewSet)
# routers.register('accounts', include('accounts.urls'))


urlpatterns = [
    path('api/', include(routers.urls)),
#     path('', include(routers.urls)),
    path('page/', PageList.as_view({'get': 'list', 'post': 'create'})),
    path('page/<int:pk>/',
         PageDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('concert/', ConcertList.as_view({'get': 'list', 'post': 'create'})),
    path('concert/recent/', ConcertRecent.as_view()),
    path('concert/near/', ConcertNear.as_view()),
    path('concert/<int:pk>/',
         ConcertDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('concert/calender/', GetConcertListWithMonthAPI.as_view()),

    path('hashtag/', include("hashtag.urls")),

]

urlpatterns += routers.urls
