from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class post(models.Model):
    post_img = models.ImageField(default='dummy_logo.png',null=True,blank=True,upload_to = 'images')
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return str(self.id)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)