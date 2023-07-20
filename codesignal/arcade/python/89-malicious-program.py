import re
import calendar
from collections import deque

short_months = [month_name[:3] for month_name in calendar.month_name[1:]]

def solution(current_date, changes):
    months = deque(short_months, maxlen=12)
    
    matches = re.match(
        '(\d{2}) ([a-zA-Z]{3}) (\d{4}) (\d{2}):(\d{2}):(\d{2})',
        current_date
    )
    groups = matches.groups()
    
    day = int(groups[0])
    month_index = months.index(groups[1])
    month = months.rotate(len(months) - month_index) or months
    year = int(groups[2])
    hours = int(groups[3])
    minutes = int(groups[4])
    seconds = int(groups[5])

    new_date = [
        part + change if not isinstance(part, deque) else part.rotate(-change) or part[0]
        for (part, change) in zip([day, month, year, hours, minutes, seconds], changes)
    ]

    new_month_index = short_months.index(new_date[1])
    if new_date[0] < 0 or new_date[0] > calendar.monthrange(new_date[2], new_month_index + 1)[1]:
        return current_date
    if (changes[1] > 0 and new_month_index < month_index) or (changes[1] < 0 and new_month_index > month_index):
        return current_date
    if new_date[2] < 0:
        return current_date
    if new_date[3] < 0 or new_date[3] > 23:
        return current_date
    if new_date[4] < 0 or new_date[4] > 59:
        return current_date
    if new_date[5] < 0 or new_date[5] > 59:
        return current_date

    return f"{new_date[0]:02d} {new_date[1]} {new_date[2]:4d} {new_date[3]:02d}:{new_date[4]:02d}:{new_date[5]:02d}"
    
