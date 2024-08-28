from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, home, upload_resume

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('upload_resume/', upload_resume, name='upload_resume'),
]
