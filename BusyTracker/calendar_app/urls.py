from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view_url'),
]
