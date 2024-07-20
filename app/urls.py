from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    
    path('students/', views.students),
    path('students/<int:stud_id>/', views.detail, name='stud_detail'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('more/', views.more, name='more'),
    path('animals/', views.animals, name='animals')
]