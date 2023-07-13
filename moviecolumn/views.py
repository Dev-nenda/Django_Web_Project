from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

from .models import Moviecolumn, Comment
from .forms import MoviecolumnForm, CommentForm



@login_required
@require_http_methods(['GET', 'POST'])
def create_moviecolumn(request):
    # expert_movie 그룹이 아니면 홈으로 가게 만듬
    if not request.user.groups.filter(name="expert_movie").exists():
        return redirect('home')
    
    
    if request.method == 'GET':
        form  = MoviecolumnForm

    else:
        form = MoviecolumnForm(request.POST)
        if form.is_valid():
            moviecolumn = form.save(commit=False)
            moviecolumn.author = request.user
            moviecolumn.save()

            return redirect('moviecolumn:moviecolumn_detail', moviecolumn.pk)
        
    return render(request, 'moviecolumn/form.html', {
        'form' : form, 
    })


@require_safe
def moviecolumn_index(request):
    moviecolumns = Moviecolumn.objects.all()
    return render(request, 'moviecolumn/index.html', {
        'moviecolumns' : moviecolumns
    })


@require_safe
def moviecolumn_detail(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)

    form = CommentForm
    is_like = moviecolumn.like_users.filter(pk=request.user.pk).exists()
    is_clipping = moviecolumn.clipping_users.filter(pk=request.user.pk).exists()
    comments = moviecolumn.comments.all()

    moviecolumn.hits +=1
    moviecolumn.save()

    return render(request, 'moviecolumn/detail.html', {
        'moviecolumn' : moviecolumn,
        'form' : form,
        'is_like' : is_like,
        'is_clipping' : is_clipping,
        'comments': comments,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update_moviecolumn(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)

    if request.user != moviecolumn.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    if request.method == 'GET':
        form = MoviecolumnForm(instance=moviecolumn)
    
    else: 
        form = MoviecolumnForm(request.POST, instance=moviecolumn)
        if form.is_valid():
            moviecolumn=form.save()
            return redirect('moviecolumn:moviecolumn_detail', moviecolumn.pk)
    return render(request, 'moviecolumn/form.html',{
        'form': form,
    })

@login_required
@require_POST
def delete_moviecolumn(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)

    if request.user != moviecolumn.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    moviecolumn.delete()
    return redirect('moviecolumn:moviecolumn_index')

@login_required
@require_POST
def create_comment(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.moviecolumn = moviecolumn
        comment.author = request.user
        comment.save()

        return redirect('moviecolumn:moviecolumn_detail', moviecolumn.pk)
    
@login_required
@require_POST
def delete_comment(request, moviecolumn_pk, comment_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    comment.delete()
    return redirect('moviecolumn:moviecolumn_detail', moviecolumn.pk)

@login_required
@require_POST
def like_moviecolumn(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)
    user = request.user

    if moviecolumn.like_users.filter(pk=user.pk).exists():
        moviecolumn.like_users.remove(user)
    
    else:
        moviecolumn.like_users.add(user)

    return redirect('moviecolumn:moviecolum_detail', moviecolumn.pk)

def clipping_moviecolumn(request, moviecolumn_pk):
    moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)
    user = request.user

    if moviecolumn.clipping_users.filter(pk=user.pk).exists():
        moviecolumn.clipping_users.remove(user)

    else:
        moviecolumn.clipping_users.add(user)

    return redirect('moviecolumn:moviecolumn_detail', moviecolumn.pk)



