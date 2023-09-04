
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newpost/', views.newpost, name='newpost'),
    path('profile/<int:user_ident>', views.profile, name='profile'),
    path('follow/', views.follow, name='follow'),
    path('unfollow/', views.unfollow, name='unfollow')

]
