from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('form/', views.submit_form,name="submit_form"),
    path('django_form/', views.StudentForm,name="django_form"),
    path('django_form/', views.PasswordValidationProject,name="django_form"),
    
]
