from django.urls import path 
from playground import views

# URL configuration module
# Import into main url config module
urlpatterns = [
    path('hello/', views.say_hello)
]