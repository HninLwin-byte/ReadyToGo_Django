from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation/', views.reservation, name='reservation'),
    path('home/', views.home, name='home')
]