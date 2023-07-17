from django.shortcuts import render
from django.views.decorators.http import require_safe
from exhibition.models import Exhibition
from movie.models import Movie
from moviecolumn.models import Moviecolumn
from art.models import Art



# Create your views here.

@require_safe
def home(request):
    movies = Movie.objects.all()
    exhibitions = Exhibition.objects.all()

    return render(request, 'home/home.html',{
        'movies': movies,
        'exhibitions' : exhibitions,
    })

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        movies = Movie.objects.filter(title__contains=searched)
        exhibitions = Exhibition.objects.filter(title__contains=searched)
        moviecolumns = Moviecolumn.objects.filter(title__contains=searched)
        arts = Art.objects.filter(title__contains=searched)
        return render(request, 'home/searched.html',{
             'searched': searched,
             'movies': movies,
             'exhibitions': exhibitions,
             'moviecolumns': moviecolumns,
             'arts': arts,
             })
        
    else:
            return render(request, 'home/searched.html', {})