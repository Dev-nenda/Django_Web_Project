from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

from .models import Moviecolumn, Comment
from .forms import MoviecolumnForm, CommentForm



@login_required
@require_http_methods(['GET', 'POST'])
def create_moviecolumn(request):
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

    return render(request, 'moviecolumn/detail.html', {
        'moviecolumn' : moviecolumn,
        'form' : form,
        'is_like' : is_like,
        'is_clipping' : is_clipping,
        'comments': comments,
    })

# def update_moviecolumn(request, moviecolumn_pk):
#     moviecolumn = get_object_or_404(Moviecolumn, pk=moviecolumn_pk)

#     if request.user != moviecolumn.author:
#         from django.http import HttpResponseBadRequest
#         return HttpResponseBadRequest('안돼요!!')
    
#     if request.method == 'GET':
#         form = MoviecolumnForm(instance=moviecolumn)
    
#     else: 
#         form = MoviecolumnForm(request.POST, instance=moviecolumn)

