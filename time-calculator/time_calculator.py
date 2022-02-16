def add_minutes(start_min, duration_min):
    end_min = int(start_min) + int(duration_min)

    if end_min > 59:
        end_min -= 60
        return end_min, 1

    return end_min, 0

def same_period():
    if end_hours < 12: # in the same period
        return f"{str(end_hours)}:{str(end_minutes)} {period}"

def add_time(start_time, duration, starting_day=''):
    periods = ('PM', 'AM')
    end_minutes = 0
    end_hours = 0
    new_period = ''
    new_time = ''

    # split start_time
    time, period = start_time.split(' ')
    start_hours, start_minutes = time.split(':')

    # split duration
    duration_hours, duration_minutes = duration.split(':')

    # add minutes
    end_minutes, end_hours = add_minutes(start_minutes, duration_minutes)

    # add hours
    end_hours += int(start_hours) + int(duration_hours)

    if end_hours < 12: # in the same period
        return f"{str(end_hours)}:{str(end_minutes)} {period}"

    if end_hours == 12:
        if 'PM' == period:
            new_period = 'AM'
        else:
            new_period = 'PM'

        if starting_day:
            return f"{str(end_hours)}:{str(end_minutes)} {new_period} {starting_day}"
        else:
            return f"{str(end_hours)}:{str(end_minutes)} {new_period}"

    if end_hours > 12 and end_hours <= 24:
        end_hours -= 12
        if 'PM' == period:
            new_period = 'AM'
        else:
            new_period = 'PM'

        return f"{str(end_hours)}:{str(end_minutes)} {new_period} (next day)"

    n_days = int(end_hours / 12)
    end_hours -= n_days * 12

    if n_days % 2 == 0:
        if 'PM' == period:
            new_period = 'AM'
            return f"{str(end_hours)}:{str(end_minutes)} {new_period} ({n_days/2} days later)"

    return f"{str(end_hours)}:{str(end_minutes)} {period} ({n_days/2} days later)"

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
