from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import User


from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm

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


def set_general_permission(request):
    if request.user.groups.exists() == True:
        return redirect('home')
    else:
        group= Group.objects.get(name='general')
        request.user.groups.add(group)
        
        return redirect('home')



@require_http_methods(['GET', 'POST'])
def delete(request, username):
    profile_user = get_object_or_404(User, username = username)
    if request.user == profile_user:
        request.user.delete()
        auth_logout(request)
    return redirect('home')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, username):
    profile_user = get_object_or_404(User, username=username)
    if request.user == profile_user:
        
        
        if request.method == 'GET':
            form = CustomUserChangeForm(instance=request.user)

        else:
            form =CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()

                return redirect('account:profile', profile_user.username)
            
        return render(request, 'accounts/update.html', {
            'form' : form
        })
    

@login_required
def change_password(request, username):
    profile_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('account:profile', request.user.username)
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {
        'password_change_form':password_change_form
        })
    
    


