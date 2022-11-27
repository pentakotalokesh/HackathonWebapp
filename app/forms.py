from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import post

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'
class postForm(ModelForm):

        class Meta:
            model=post
            fields = ['post_img']
        