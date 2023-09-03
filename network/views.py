from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import post, User, fllow




def index(request):
    all_posts = post.objects.all().order_by('id').reverse() 
    paginator = Paginator(all_posts, 1)
    page_num = request.GET.get('page')
    post_page = paginator.get_page(page_num) 

    return render(request, "network/index.html", {
        'all_posts': all_posts,
        'post_page': post_page
    })


def newpost(request):
    if request.method == 'POST':  
        content = request.POST['content']
        user = User.objects.get(pk=request.user.id)
        new_post = post(content=content, user=user)
        new_post.save()
        
        return HttpResponseRedirect(reverse('index'))
    

def profile(request, user_ident):
    user_obj= User.objects.get(pk=user_ident)
    all_posts = post.objects.filter(user=user_obj).order_by('id').reverse() 
    following= fllow.objects.filter(user_fllower=user_obj)
    follower= fllow.objects.filter(user_fllowed=user_obj)
    paginator = Paginator(all_posts, 1)
    page_number = request.GET.get('page')
    post_page = paginator.get_page(page_number) 

    return render(request, "network/profile.html", {
        'all_posts': all_posts,
        'post_page': post_page,
        'username': user_obj.username,
        'following':following,
        'follower': follower


    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
