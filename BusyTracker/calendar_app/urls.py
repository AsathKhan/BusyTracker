from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view_url'),
    path('add/', views.add_reminder, name='add_reminder_url'),
    path('<int:year>/<int:month>/<int:day>/', views.reminder_by_date, name='reminder_by_date'),  # Reminders for a specific date

]
