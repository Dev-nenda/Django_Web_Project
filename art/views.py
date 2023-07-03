from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Art, Comment
from .forms import ArtForm, CommentForm

@login_required
@require_http_methods(['GET', 'POST'])
def create_art(request):
    if request.method =='GET':
        form = ArtForm

    else: 
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.save()

            return redirect('art:art_detail', art.pk)
    return render(request, 'art/form.html', {
        'form': form,
    })

@require_safe
def art_index(request):
    arts = Art.objects.all()
    return render(request, 'art/index.html', {
        'arts' : arts,
    })

@require_safe
def art_detail(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)
    form = CommentForm
    is_like = art.like_users.filter(pk=request.user.pk).exists()
    is_clipping = art.clipping_users.filter(pk=request.user.pk).exists()
    comments = art.comments.all()
    return render(request, 'art/detail.html', {
        'art': art,
        'comments': comments,
        'form': form,
        'is_like' : is_like,
        'is_clipping': is_clipping
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_art(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)

    if request.user != art.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    if request.method == 'GET':
        form = ArtForm(instance=art)
    
    else:
        form = ArtForm(request.POST, instance=art)
        if form.is_valid():
            art=form.save()
            return redirect('art:art_detail', art.pk)
    return render(request, 'art/form.html', {
        'form' : form,
    })

@login_required
@require_POST
def delete_art(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)

    if request.user != art.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    art.delete()
    return redirect('art:art_index')
    
@login_required
@require_POST
def create_comment(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.art = art
        comment.author =request.user
        comment.save()

        return redirect('art:art_detail', art.pk)
    
@login_required
@require_POST
def delete_comment(request, art_pk, comment_pk):
    art = get_object_or_404(Art, pk=art_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    comment.delete()
    return redirect('art:art_detail', art.pk)


@login_required
@require_POST
def like_art(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)
    user = request.user

    if art.like_users.filter(pk=user.pk).exists():
        art.like_users.remove(user)
    
    else:
        art.like_users.add(user)
    
    return redirect('art:art_detail', art.pk)

@login_required
@require_POST
def clipping_art(request, art_pk):
    art = get_object_or_404(Art, pk=art_pk)
    user = request.user

    if art.clipping_users.filter(pk=user.pk).exists():
        art.clipping_users.remove(user)
    
    else:
        art.clipping_users.add(user)
    
    return redirect('art:art_detail', art.pk)    
    

