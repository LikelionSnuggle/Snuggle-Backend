from django.contrib import admin
from django.urls import path, include

from .views import UserViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)
# routers.register('perfoemance', PerformanceViewSet)
# routers.register('page', PageViewSet)
# routers.register('pageinfo', PageInfoViewSet)
# routers.register('pagenotification', PageNotificationViewSet)
# routers.register('preformancelist', PerformanceListViewSet)
# routers.register('calender', CalenderViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]