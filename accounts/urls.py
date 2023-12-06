
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signupAPIView, LoginAPIView, Cu
from django.contrib import admin


app_name = 'accounts'
urlpatterns = [ 
    path('signup/', signupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    # path('login', views.login),

# from django.urls import path, include

# urlpatterns = [
#     path('', include('dj_rest_auth.urls')),
#     path('registration/', include('dj_rest_auth.registration.urls')),
]
