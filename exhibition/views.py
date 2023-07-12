from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Exhibition, Expert_review, General_review
from .forms import ExhibitionForm, Expert_reviewForm, General_reviewForm

from django.db.models import Avg


@login_required
@require_http_methods(['GET','POST'])
def create_exhibition(request):
    # gallery 그룹이 아니면 홈으로 가게 만듬
    if not request.user.groups.filter(name="gallery").exists():
        return redirect('home')
    
    if request.method == 'GET':
        form = ExhibitionForm()

    else:
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.owner = request.user
            exhibition.save()

            return redirect('exhibition:exhibition_detail', exhibition.pk)
    
    return render(request, 'exhibition/form.html', {
        'form' : form
    })

@require_safe
def exhibition_index(request):
    exhibitions = Exhibition.objects.all()

    return render(request, 'exhibition/index.html',{
        'exhibitions': exhibitions
    })

@require_safe
def exhibition_detail(request, exhibition_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)
    expert_form = Expert_reviewForm()
    general_form = General_reviewForm()
    is_like = exhibition.like_users.filter(pk=request.user.pk).exists()

    expert_scores = 0.0
    expert_score = Expert_review.objects.filter(exhibition_id = exhibition.pk).aggregate(average_score=Avg("score"))
    if expert_score['average_score'] != None:
        expert_scores = expert_score['average_score']
        
    
    general_scores = 0.0
    general_score = General_review.objects.filter(exhibition_id = exhibition.pk).aggregate(average_score=Avg("score"))
    if general_score['average_score'] != None:
        general_scores = general_score['average_score']


    exeprt_reviews = exhibition.expert_reviews.all()
    general_reviews = exhibition.general_reviews.all()

    exhibition.score = general_scores

    exhibition.hits +=1
    exhibition.save()

    return render(request, 'exhibition/detail.html', {
        'exhibition' : exhibition,
        'expert_reviews': exeprt_reviews,
        'general_reviews': general_reviews,
        'expert_form': expert_form,
        'general_form': general_form,
        'is_like' : is_like,
        'expert_score': expert_scores,
        'general_score': general_scores,
        
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_exhibition(request, exhibition_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)

    if request.user != exhibition.owner:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    if request.method == 'GET':
        form = ExhibitionForm(instance=exhibition)

    else:
        form = ExhibitionForm(request.POST, instance=exhibition)
        if form.is_valid():
            exhibition=form.save()
            return redirect('exhibition:exhibition_detail', exhibition.pk)
    return render(request, 'exhibition/form.html', {
        'form' : form,
    }) 

@login_required
@require_POST
def delete_exhibition(request, exhibition_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)

    if request.user != exhibition.owner:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    exhibition.delete()
    return redirect('exhibition:exhibition_index')

    
@login_required
@require_POST
def create_expert_review(request, exhibition_pk):
    # expert_art 그룹이 아니면 홈으로 가게 만듬
    if not request.user.groups.filter(name="expert_art").exists():
        return redirect('home')
    
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)
    
    expert_form = Expert_reviewForm(request.POST)
    if expert_form.is_valid():
        expert_review = expert_form.save(commit=False)
        expert_review.exhibition = exhibition
        expert_review.author = request.user
        expert_review.save()

        return redirect('exhibition:exhibition_detail', exhibition.pk)

@login_required
@require_POST
def delete_expert_review(request, exhibition_pk, expert_reviews_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)
    expert_review = get_object_or_404(Expert_review, pk=expert_reviews_pk)

    if request.user != expert_review.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    expert_review.delete()
    return redirect('exhibition:exhibition_detail', exhibition.pk)

@login_required
@require_POST
def create_general_review(request, exhibition_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)

    general_form = General_reviewForm(request.POST)
    if general_form.is_valid():
        general_review = general_form.save(commit=False)
        general_review.exhibition = exhibition
        general_review.author = request.user
        general_review.save()

        return redirect('exhibition:exhibition_detail', exhibition.pk)
@login_required
@require_POST
def delete_general_review(request, exhibition_pk, general_reviews_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)
    general_review = get_object_or_404(General_review, pk=general_reviews_pk)

    if request.user != general_review.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    general_review.delete()
    return redirect('exhibition:exhibition_detail', exhibition.pk)


@login_required
@require_POST
def like_exhibition(request, exhibition_pk):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_pk)
    user = request.user

    if exhibition.like_users.filter(pk=user.pk).exists():
        exhibition.like_users.remove(user)
    
    else:
        exhibition.like_users.add(user)

    return redirect('exhibition:exhibition_detail', exhibition.pk)



