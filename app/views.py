from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import post,Like
from . forms import postForm
# Create your views here.
from .forms import CreateUser

def index(request):
    return render(request,'app/index.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/Sign_up.html', {'form': form})

def login_page(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('post')
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('post')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None and not user.is_superuser:
            login(request,user)
            return redirect('post')
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('post')
        else:
            messages.error(request,'Invalid login')
        

    return render(request,'app/Login.html')
def post_page(request):
    if request.user.is_authenticated:
        user = request.user
        form = postForm()
        if request.method == 'POST':
            form = postForm(request.POST,request.FILES)
            if form.is_valid():
                cu = form.save(commit=False)
                cu.user = user
                cu.save()
            return redirect('post')
        listpost= post.objects.all()
        context = {'posts':listpost,'form':form}
        return render(request,'app/postpage.html',context)
    else:
        return render(request,'app/Login.html')

def Deletepost(request, pk):
    p = post.objects.get(id=pk)
    if request.method == 'POST':
        p.delete()
        return redirect('post')
    return render(request, 'app/delete.html', {'obj': p})

def Updatepost(request, pk):
    p = post.objects.get(id=pk)
    form = postForm(instance=p)
    if request.method == 'POST':
        form = postForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('post')
    context = {'form': form}

    return render(request, 'app/edit.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

