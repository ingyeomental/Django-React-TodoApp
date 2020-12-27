from django.urls import path
from . import views


urlpatterns = [
    path('', views.servicepage, name='servicepage'),
]