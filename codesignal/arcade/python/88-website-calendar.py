import calendar

def solution(month, year):
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    month_name = calendar.month_name[month]
    headers = ''.join(f'<th class="{day}">{day.capitalize()}</th>' for day in days)
    weeks = [
        ''.join(
            f'<td class="{days[i]}">{day}</td>' if day != 0 else '<td class="noday">&nbsp;</td>' 
            for i, day in enumerate(week)
        )
        for week in calendar.monthcalendar(year, month)
    ]

    content = (
        f'<tr><th colspan="7" class="month">{month_name} {year}</th></tr><tr>{headers}</tr>' +
        ''.join(f'<tr>{week}</tr>' for week in weeks)
    )
    
    return f'<table border="0" cellpadding="0" cellspacing="0" class="month">{content}</table>'