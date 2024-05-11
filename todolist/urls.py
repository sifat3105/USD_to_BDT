from django.urls import path
from .views import dolist_func

urlpatterns = [
    path('dolist_func',dolist_func, name= 'dolist_func')
]
