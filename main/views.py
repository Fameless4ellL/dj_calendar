import calendar
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
async def index(request, year: int = datetime.now().year, month: int = datetime.now().month):
    next_month = datetime(year, month, 1) + timedelta(days=31)
    prev_month = datetime(year, month, 1) - timedelta(days=1)
    context = {
        'calendar_title': f"{calendar.month_name[month]} {str(year)}",
        'calendar_current': datetime(year, month, 1).month == datetime.now().month,
        "calendar_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        'calendar_body': calendar.monthcalendar(year, month),
        'calendar_next_month': f'{next_month.year}_{next_month.month}',
        'calendar_prev_month': f'{prev_month.year}_{prev_month.month}',
        'calendar_now': datetime.now()
    }
    return render(request, 'main/index.html', context)
