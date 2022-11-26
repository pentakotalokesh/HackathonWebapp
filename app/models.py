from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class post(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    post_img = models.ImageField(default='dummy_logo.png',null=True,blank=True,upload_to = 'images')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_like')