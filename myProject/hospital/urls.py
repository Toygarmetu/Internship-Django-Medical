# pages/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path('appointment/', views.book_appointment, name='appointment'),
    path('doctors/', views.doctors, name='doctors'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('index/', views.index, name='index'),
    path('medicines/', views.medicines, name='medicines')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)