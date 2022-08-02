from django.contrib import admin
from django.urls import path
from myapp import views 


urlpatterns = [
    path("", views.base, name='base'),
    path("contact", views.Contact, name='Contact'),
]
