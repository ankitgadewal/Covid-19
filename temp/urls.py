from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('apis/', views.apis),
    path('postapi/', views.postapis)
]
