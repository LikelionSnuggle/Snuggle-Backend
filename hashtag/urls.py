from django.urls import path

from . import views 

app_name = "hashtag"

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:hash_pk>/', views.hashtag, name ='hashtag'),
]