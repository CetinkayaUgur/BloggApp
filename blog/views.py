from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm
from .models import Post

def home_view(request):
    posts = Post.objects.filter(is_deleted = True)

    context = dict(
        posts = posts,
    )

    return render(request, 'blog/posts_list.html', context)

def login_view(request):
    return render(request, 'blog/login.html', {})

@csrf_protect
def register_view(request):
    if request.user.is_authenticated :
            messages.info(request, 'Zaten bir hesapla giriş yaptın!')
            return redirect('/')
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        print("*****")
        username =  form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        #buraya kadar sıkıntı yok işleme kısmına karar ver


        newUser = User(username = username)
        if User.objects.filter(username = username).first():
            messages.info(request, "Bu kullanıcı adı daha önce alındı")
            return redirect('/')
    
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, 'Bravo kaydoldun!')
        return redirect('/')
    
    context = {
        'form' : form
    }
    
    return render(request, 'blog/register.html', context)

def profile_view(request):
    return render(request, 'blog/profile.html', {})
