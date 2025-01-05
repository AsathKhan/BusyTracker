from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import now
from calendar import Calendar
from datetime import date
from .models import Reminder

# Create your views here.
def calendar_view(request, year=None, month=None):
    """Display the calendar for a specific month and year."""
    if not year or not month:
        today = date.today()
        year = today.year
        month = today.month

    cal = Calendar()
    month_calendar = cal.monthdayscalendar(year, month)

    # Get reminders for the current month
    reminders = Reminder.objects.filter(date__year=year, date__month=month)

    return render(request, "calendar_app/calendar.html", {
        "month_calendar": month_calendar,
        "year": year,
        "month": month,
        "reminders": reminders
    })
    
def add_reminder(request):

    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time", None)
        description = request.POST.get("description")

        Reminder.objects.create(date=date, time=time, description=description)
        return redirect("calendar_view_url")

    return render(request, "calendar_app/add_reminder.html")

def reminder_by_date(request, year, month, day):
    """View reminders for a specific date."""
    reminders = Reminder.objects.filter(date__year=year, date__month=month, date__day=day)
    return render(request, "calendar_app/reminders_by_date.html", {
        "year": year,
        "month": month,
        "day": day,
        "reminders": reminders
    })