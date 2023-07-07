from django.shortcuts import render
from django.views.decorators.http import require_safe
from exhibition.models import Exhibition
from movie.models import Movie


# Create your views here.

@require_safe
def home(request):
    movies = Movie.objects.all()
    exhibitions = Exhibition.objects.all()

    return render(request, 'home/home.html',{
        'movies': movies,
        'exhibitions' : exhibitions,
    })

