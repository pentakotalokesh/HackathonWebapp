from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name='logout'),
    path('postpage/',views.post_page,name='post'),
    path('delete-Person/<str:pk>/',views.Deletepost,name="DeletePerson"),
    path('update-person/<str:pk>/',views.Updatepost,name="UpdatePerson"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)