from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signupAPIView
from django.contrib import admin


app_name = 'accounts'
urlpatterns = [
    path('signup/', signupAPIView.as_view()),
    # path('login', views.login),
]
