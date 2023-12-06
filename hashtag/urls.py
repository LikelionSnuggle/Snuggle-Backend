from django.urls import path

from . import views 

app_name = "hashtag"

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.HashtagAPIView.as_view(), name ='hashtag'),
]