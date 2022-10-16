import calendar
from datetime import datetime, timedelta

from asgiref.sync import async_to_sync
from django.shortcuts import render
from main.models import Event


@async_to_sync
async def index(request, year: int = datetime.now().year, month: int = datetime.now().month, group: str = None):
    events = Event.objects.select_related()
    choice_list = events.values_list('group__name', flat=True)
    choice = {}
    if len(choice_list) > 0:
        if group:
            choice = {'default': group, 'choice': list(choice_list)}
        else:
            choice = {'default': choice_list[0], 'choice': list(choice_list)}
    else:
        choice['default'] = None

    if group is None:
        event_group = events.filter(date__year=year, date__month=month)
    else:
        event_group = events.filter(date__year=year, date__month=month, group__name=group)

    next_month = datetime(year, month, 1) + timedelta(days=31)
    prev_month = datetime(year, month, 1) - timedelta(days=1)
    context = {
        'calendar_title': f"{calendar.month_name[month]} {str(year)}",
        'calendar_current': datetime(year, month, 1).month == datetime.now().month,
        'calendar_week': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        'calendar_body': calendar.monthcalendar(year, month),
        'calendar_next_month': f'{next_month.year}_{next_month.month}_{choice["default"]}',
        'calendar_prev_month': f'{prev_month.year}_{prev_month.month}_{choice["default"]}',
        'calendar_now': datetime.now(),
        'choice': choice,
        'events': event_group,
    }
    return render(request, 'main/index.html', context)
