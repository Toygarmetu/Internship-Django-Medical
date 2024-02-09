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
    path('medicines/', views.medicines, name='medicines'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('diseases/', views.diseases, name='diseases'),
    path('patient/<int:patient_id>/add_medical_history/', views.add_medical_history, name='add_medical_history'),
    path('patient_profile/<int:patient_id>', views.patient_profile, name='patient_profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)