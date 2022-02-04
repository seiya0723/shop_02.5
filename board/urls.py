from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.Home, name='home'),
    path('category', views.Category, name='category')
]