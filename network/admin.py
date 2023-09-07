from django.contrib import admin
from .models import post,User,fllow,Like

# Register your models here.
admin.site.register(post)
admin.site.register(User)
admin.site.register(fllow)
admin.site.register(Like)