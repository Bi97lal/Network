from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import post
from .models import User, fllow
from django.core.paginator import Paginator


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

    user_obj = User.objects.get(pk=user_ident)
    all_posts = post.objects.filter(user=user_obj).order_by('id').reverse()
    following = fllow.objects.filter(user_fllower=user_obj)
    follower = fllow.objects.filter(user_fllowed=user_obj)
    try:
        checking = follower.filter(
            user_obj=User.objects.get(pk=request. user_obj.id))
        if len(checking) != 0:
            follow_you = True
        else:
            follow_you = False
    except:
        follow_you = False

    paginator = Paginator(all_posts, 1)
    page_number = request.GET.get('page')
    post_page = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        'all_posts': all_posts,
        'post_page': post_page,
        'username': user_obj.username,
        'following': following,
        'follower': follower,
        'follow_you': follow_you,
        "user_obj_profile": user_obj,



    })


def follow(request):
    userfollow = request.POST['userfollow']
    currentuser = User.objects.get(pk=request.user.id)
    userfollowdata = User.objects.get(username=userfollow)
    f = follow(user=currentuser, usserfollowed=userfollowdata)
    f.save()
    user_id = userfollowdata.id
    return HttpResponseRedirect(reverse(profile, kwargs={"user_id": user_id}))


def following(request):
    current_user = User.objects.get(pk=request.user.id)
    following_all_people = fllow.objects.filter(user_fllower=current_user)

    all_posts_following = post.objects.all().order_by('id').reverse()

    following_poster = []
    for current_post in all_posts_following:
        for person in following_all_people:
            if person.user_fllowed == current_post.user:
                following_poster.append(post)

    paginator = Paginator(following_poster, 1)
    page_num = request.GET.get('page')
    post_page = paginator.get_page(page_num)

    user_obj = request.user

    return render(request, "network/following.html", {
        'post_page': post_page,
        'user_obj': user_obj,
    })



def unfollow(request):
    userfollow = request.POST['userfollow']
    currentuser = User.objects.get(pk=request.user.id)
    userfollowdata = User.objects.get(username=userfollow)
    f = follow.objects.get(user=currentuser, userfollow=userfollowdata)
    f.delete()

    user_id = userfollowdata.id
    return HttpResponseRedirect(reverse(profile, kwargs={"user_id": user_id}))



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
