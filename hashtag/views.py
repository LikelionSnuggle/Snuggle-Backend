from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hashtag index")

def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    movies = hashtag.movie_set.order_by('-pk')
    context = {
        'hashtag': hashtag, 
        'movies': movies,
    }
    return render(request, 'hashtag.html', context)