from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    pass



class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} by {self.user.username} on {self.date.strftime('%D %B %Y %H:%M:%S')}"

     
class fllow(models.Model):
    user_fllower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_is_fllowing")
    user_fllowed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_you_fllowed")

    def __str__(self):
        return f"{self.user_fllower} Following {self.user_fllowed}"
    
class Like(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_like")
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_post_like")
        
    def __str__(self):
        return f"{self.user} Liked {self.post}" 




     