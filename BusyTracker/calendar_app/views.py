from django.shortcuts import render

# Create your views here.
def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')