from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('test.html', views.about, name="about"),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("icons.html", views.icons, name="icons"),
    path("mens.html", views.mens, name="mens"),
    path("womens.html", views.womens, name="womens"),
    path("single.html", views.single, name="single"),
    path("typography.html", views.typography, name="typography"),
]
