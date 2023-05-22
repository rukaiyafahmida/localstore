from django.urls import path
from . import views


# URLConf Module
urlpatterns = [
    path('hello/', views.say_hello)
]