from django.urls import path

from . import views


urlpatterns = [
    path("", views.Mi_familia,  name= "index"),
    
]