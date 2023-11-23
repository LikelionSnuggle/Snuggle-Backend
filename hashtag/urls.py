from django.urls import path

from . import views 

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:hash_pk>/', views.hashtag, name ='hashtag'),
]