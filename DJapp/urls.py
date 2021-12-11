from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("restaurants/", views.restaurants, name="restaurants"),
    
    path("pricing/", views.pricing, name="pricing"),
    path("portfolio/", views.portfolio, name="portfolio"),
    
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact")    
    
    #path("post/<str:p>",views.post, name="post")
    
]