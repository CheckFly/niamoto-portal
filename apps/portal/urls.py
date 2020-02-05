# coding: utf-8

from django.urls import include, path
from .views import home, methodologie, RessouresView

urlpatterns = [
    path('', home, name="home"),
    path('methodologie/', methodologie, name="methodologie"),
    path('ressources/', RessouresView.as_view(), name="ressources"),
]
