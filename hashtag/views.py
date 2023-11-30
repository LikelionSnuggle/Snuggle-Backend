from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append("../django_back")
from django_back import models

from . import serializers

from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hashtag index")

def hashtag(request, hash_pk):
    hashtag = get_object_or_404(models.Hashtag, pk=hash_pk)
    concerts = hashtag.concert_set.order_by('-pk')
    context = {
        'hashtag': hashtag, 
        'concert': concerts,
    }
    return render(request, 'hashtag.html', context)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Hashtag.objects.all()
    serializer_class = serializers.HashtagSerializer