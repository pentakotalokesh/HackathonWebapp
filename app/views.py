from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
from .forms import CreateUser
def post_page(request):
    if request.user:
        return HttpResponse("Sucess")
    else:
        return render(request,'app/Login.html')
def index(request):
    return render(request,'app/index.html')
def register(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('post')
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('user')
    form = CreateUser()
    if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registered Sucessfully")
            else:
                messages.error(request,'Invalid Registration')
    context = {'form':form}
    return render(request,'app/Sign_up.html',context)

def login_page(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('user')
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('post')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None and not user.is_superuser:
            login(request,user)
            return redirect('user')
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('post')
        else:
            messages.error(request,'Invalid login')
        

    return render(request,'app/Login.html')

# def like(request, id):
#     signed_in = request.user
#     post = Post.objects.get(id=id)

#     if signed_in and post:
#         post.like.add(signed_in)
#         # For unlike, remove instead of add
def logout_page(request):
    logout(request)
    return redirect('login')

