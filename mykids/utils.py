# calendarapp/utils.py

from datetime import datetime, timedelta
from calendar import HTMLCalendar
from kiddytalks.models import Event
from eventcalendar.helper import get_current_user


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(date_slot__day=day)
        d = ''

        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        # print('*************************** 6')
        week = ''
        for d, weekday in theweek:
            # print('*************************** ', d)
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        # print('***************************')
        events = Event.objects.filter(date_slot__year=self.year, date_slot__month=self.month)
        # print('EVENN', events)
        # events = Event.objects.all(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        # print('***************************', cal)
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        # print('*************************** 2')
        cal += f'{self.formatweekheader()}\n'
        # print('*************************** 3')
        for week in self.monthdays2calendar(self.year, self.month):
            # print('*************************** 4')
            cal += f'{self.formatweek(week, events)}\n'
            # print('*************************** 5')
        return cal
