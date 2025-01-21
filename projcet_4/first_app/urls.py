from django.urls import path
from . import views

# URL patterns for the app
urlpatterns = [
    path('', views.index, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
]
