from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append("../django_back/models.py")
from . import models

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