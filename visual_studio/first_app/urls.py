from django.contrib import admin
from django.urls import path
from first_app.views import hello_world

urlpatterns = [
    path('', hello_world)
]