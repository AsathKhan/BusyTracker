from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.timezone import now
from calendar import Calendar
from datetime import date, timedelta
from .models import Reminder

# Create your views here.
def calendar_view(request, year=None, month=None):
    today = date.today()

    # Default to the current month and year if not provided
    if year is None or month is None:
        year = today.year
        month = today.month

    year, month = int(year), int(month)

    # Handle navigation for previous and next months
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    # Generate calendar
    cal = Calendar()
    month_calendar = cal.monthdayscalendar(year, month)

    # Get reminders for the current month
    reminders = Reminder.objects.filter(date__year=year, date__month=month)
    reminder_dates = {r.date.day for r in reminders}

    return render(request, "calendar_app/calendar.html", {
        "month_calendar": month_calendar,
        "year": year,
        "month": month,
        "reminder_dates": reminder_dates,
        "prev_year": prev_year,
        "prev_month": prev_month,
        "next_year": next_year,
        "next_month": next_month,
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