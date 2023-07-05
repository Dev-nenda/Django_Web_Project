from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Movie, Expert_review, General_review
from .forms import MovieForm, Expert_reviewForm, General_reviewForm

from django.db.models import Avg


@login_required
@require_http_methods(['GET','POST'])
def create_movie(request):
    if request.method == 'GET':
        form = MovieForm()

    else: 
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.writer = request.user
            movie.save()

            return redirect('movie:movie_detail', movie.pk)
    
    return render(request, 'movie/form.html', {
        'form' : form
    })

@require_safe
def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html',{
        'movies': movies
    })

@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    expert_form = Expert_reviewForm()
    general_form = General_reviewForm()
    is_like = movie.like_users.filter(pk=request.user.pk).exists()
    expert_score = Expert_review.objects.aggregate(average_score=Avg("score"))
    general_score = General_review.objects.aggregate(average_score=Avg("score"))
    expert_reviews = movie.movie_expert_reviews.all()
    general_reviews = movie.movie_general_reviews.all()

    return render(request, 'movie/detail.html', {
        'movie' : movie,
        'expert_reviews': expert_reviews,
        'general_reviews': general_reviews,
        'expert_form': expert_form,
        'general_form' : general_form,
        'is_like' : is_like,
        'expert_score': expert_score['average_score'],
        'general_score': general_score['average_score'],
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.user != movie.writer:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    if request.method == 'GET':
        form = MovieForm(instance=movie)

    else:
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie=form.save()
            return redirect('movie:movie_detail', movie.pk)
    return render(request, 'movie/form.html', {
        'form' : form,
    })

@login_required
@require_POST
def delete_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.user != movie.writer:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    movie.delete()
    return redirect('movie:movie_index')

@login_required
@require_POST
def create_expert_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    expert_form = Expert_reviewForm(request.POST)
    if expert_form.is_valid():
        expert_review = expert_form.save(commit=False)
        expert_review.movie = movie
        expert_review.author = request.user
        expert_review.save()

        return redirect('movie:movie_detail', movie.pk)

@login_required
@require_POST   
def delete_expert_review(request, movie_pk, expert_review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    expert_review = get_object_or_404(Expert_review, pk=expert_review_pk)

    if request.user != expert_review.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')

    expert_review.delete()
    return redirect('movie:movie_detail', movie.pk)

@login_required
@require_POST
def create_general_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    general_form = General_reviewForm(request.POST)
    if general_form.is_valid():
        general_review = general_form.save(commit=False)
        general_review.movie = movie
        general_review.author = request.user
        general_review.save()

        return redirect('movie:movie_detail', movie.pk)
    
@login_required
@require_POST
def delete_general_review(request, movie_pk, general_review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    general_review = get_object_or_404(General_review, pk=general_review_pk)

    if request.user != general_review.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    general_review.delete()
    return redirect('movie:movie_detail', movie_pk)

def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)

    else:
        movie.like_users.add(user)

    return redirect('movie:movie_detail', movie.pk)


