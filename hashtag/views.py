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

from django.db.models import Q


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hashtag index")

class HashtagAPIView(APIView):
    def get(self, request):
#        print(hash_pk)
        tag_list = request.GET.getlist('tag')

        q_objects = Q()

        for tag in tag_list:
             q_objects |= Q(con_tag__name=tag)
        # hashtag = get_object_or_404(models.Hashtag, name=tag_list[0])
        # concerts = hashtag.concert_set.order_by('-pk')
        concerts = models.Concert.objects.filter(q_objects).order_by('-pk')
        
        serializer = ConcertListSerializer(concerts, many=True)
#        print(serializer.data)
        return Response(serializer.data)
    