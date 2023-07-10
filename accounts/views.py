from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 신규 회원가입을 할 때 general 그룹으로 설정
            group= Group.objects.get(name='general')
            user.groups.add(group)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            
            return redirect('home')
    return render(request, 'accounts/signup.html',{
        'form': form,
    })
    
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            
                
            auth_login(request, user)
            

            return redirect(request.GET.get('next') or 'home')
    return render(request, 'accounts/login.html', {
        'form': form
    })
    

def logout(request):

    auth_logout(request)
    return redirect('home')
    
@require_safe
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
    })

@login_required
@require_POST
def follow(request, username):
    star = get_object_or_404(User, username=username)
    fan = request.user

    if fan != star:
        if fan.stars.filter(pk=star.pk).exists():
            fan.stars.remove(star)
        else: 
            fan.stars.add(star)

    return redirect('account:profile', star)

@require_safe
def followers(request, username):
    profile_user = get_object_or_404(User, username=username)
    followers = profile_user.fans.all()

    return render(request, 'accounts/followers.html',{
        'followers' : followers,
    })

@require_safe
def followings(request, username):
    profile_user = get_object_or_404(User, username=username)
    followings = profile_user.stars.all()

    return render(request, 'accounts/followings.html', {
        'followings' : followings
    })

