from django.urls import path
from .views import home_func

urlpatterns = [
    path('', home_func, name='home_func')
]

