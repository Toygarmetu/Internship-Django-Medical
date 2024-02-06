# pages/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('doctors/', views.doctors, name='doctors'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]