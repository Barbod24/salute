from django.db import models
from django.contrib.auth.models import User

# class Post(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     image= models.ImageField(upload_to='pics/')
#     body= models.TextField()
#     slug= models.SlugField(max_length=100)
#     created= models.DateTimeField(auto_now_add=True)
#     updated= models.DateTimeField(auto_now=True)4
class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
    
   
    

# Create your models here.
