from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupForm, PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment, Follow
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {"form":form})


@login_required(login_url='login')
def index(request):
    posts = Post.get_all_posts()
    users = User.objects.exclude(id=request.user.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.Files)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    return render(request, 'instaapp/index.html', {'posts': posts, 'form': form, 'users': users})

    