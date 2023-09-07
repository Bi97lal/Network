
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newpost', views.newpost, name='newpost'),
    path('profile/<int:user_ident>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.unfollow, name='unfollow'),
    path('following/', views.following, name='following'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('delet_likes/<int:post_id>', views.delet_likes, name='delet_likes'),
    path('add_likes/<int:post_id>', views.add_likes, name='add_likes')

]
