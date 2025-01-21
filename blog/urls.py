from django.urls import path
from . import views  # Import your views from the blog app

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page
]
