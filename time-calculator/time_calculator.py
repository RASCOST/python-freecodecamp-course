def add_time(start_time, duration, starting_day=''):
    periods = ('PM', 'AM')
    end_minutes = 0
    end_hours = 0
    new_time = ''

    # split start_time
    time, period = start_time.split(' ')
    start_hours, start_minutes = time.split(':')

    # split duration
    duration_hours, duration_minutes = duration.split(':')

    # add minutes
    end_minutes = int(start_minutes) + int(duration_minutes)
    if end_minutes > 59:
        end_minutes -= 60
        end_hours += 1

    # add hours
    end_hours += int(start_hours) + int(duration_hours)
    if int(end_hours/12) > 2:
        end_hours = end_hours - (12 * int(end_hours/12))
    elif int(end_hours/12) > 0 and end_hours >= 13:
        new_period = periods[periods.index(period) - 1]
        end_hours = end_hours - 12
        new_time = f"{str(end_hours)}:{str(end_minutes)} AM"
        if period == 'PM':
            new_time += ' (next day)'

    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))