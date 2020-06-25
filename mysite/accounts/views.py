from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm,get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash

from django.contrib import messages

from .forms import CustomUserChangeForm, CustomUserCreationForm

from IPython import embed
 

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    # embed()
    elif request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
        
            

    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    elif request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        # AuthenticationForm은 ModelForm이 아닌 Form 상속
        # 별도로 정의된 Model이 없다는 뜻
        # 그래서 넘겨주는 인자가 달라진다.
        if form.is_valid():
            #로그인은 db에 뭔가 작성하는 것은 동일하지만, 연결된 모댈이 있는건 아닙니다.
            #그럼 무엇을 확인해야 하는가? -> 세션과 유저 정보
            auth_login(request,form.get_user())
            return redirect('articles:index')
    
    
    else:
        form =  AuthenticationForm()
        
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    
    messages.warning(request,'로그아웃 성공')
    return redirect('articles:index')
@require_POST
def delete(request):
    # if request.method="POST"
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html',context)

@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/password.html',context)


@login_required
def profile(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    context = {
        'person':person
    }
    return render(request, 'accounts/profile.html',context) 