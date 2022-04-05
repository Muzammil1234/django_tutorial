from django.urls import path
from . import views
#from .main import views

urlpatterns = [

#path("", views.index, name = "index"),

path("<int:id>", views.index, name='index'),

#path("<str:name>", views.index, name='index'),

path("", views.home, name="home")
]

