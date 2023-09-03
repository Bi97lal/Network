from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class post(models.Model):
     content=models.CharField(max_length=140)
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='auther')
     date=models.DateTimeField(auto_now_add=True)
  
  
     def __str__(self):
        return f"post {self.id} made by {self.user} on {self.date.strftime('%D %B %Y %H:%M:%S')}"
     
class fllow(models.Model):
    user_fllower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_is_fllowing")
    user_fllowed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_you_fllowed")

    def __str__(self):
        return f"{self.user_fllower} Following {self.user_fllowed}"



     