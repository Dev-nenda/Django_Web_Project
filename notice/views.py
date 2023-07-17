from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .models import Notice
from .forms import NoticeForm

@login_required
@require_http_methods(['GET', 'POST'])
def create_notice(request):
    
    if  request.user.is_superuser == False:
        return redirect('home')
    
    
    if request.method == 'GET':
        form  = NoticeForm

    else:
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('notice:notice_detail', notice.pk)
        
    return render(request, 'notice/form.html', {
        'form' : form, 
    })


@require_safe
def notice_index(request):
    notices = Notice.objects.all()
    paginator = Paginator(notices, 6)  # feeds 를 1페이지에 10개씩 묶음
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    return render(request, 'notice/index.html',{
        'page_obj': page_obj,
    })
    

@require_safe
def notice_detail(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)

    return render(request, 'notice/detail.html', {
        'notice' : notice,       
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update_notice(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)

    if request.user != notice.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    if request.method == 'GET':
        form = NoticeForm(instance=notice)
    
    else: 
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice=form.save()
            return redirect('notice:notice_detail', notice.pk)
    return render(request, 'notice/form.html',{
        'form': form,
    })

@login_required
@require_POST
def delete_notice(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)

    if request.user != notice.author:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('안돼요!!')
    
    notice.delete()
    return redirect('notice:notice_index')