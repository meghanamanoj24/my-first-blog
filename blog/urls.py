from django.urls import path
from . import views  # Import your views from the blog app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
]
