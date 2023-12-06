from django.contrib import admin

from .models import UserInfo
from rest_framework_api_key.models import APIKey

admin.register(UserInfo)

