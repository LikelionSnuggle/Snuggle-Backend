from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append("../django_back")
from django_back import models

from .serializers import HashtagSerializer
from django_back.serializers import ConcertListSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hashtag index")

class HashtagAPIView(APIView):
    def get(self, request, hash_pk):
#        print(hash_pk)
        hashtag = get_object_or_404(models.Hashtag, pk=hash_pk)
        concerts = hashtag.concert_set.order_by('-pk')
#        print(concerts)
        serializer = ConcertListSerializer(concerts, many=True)
#        print(serializer.data)
        return Response(serializer.data)