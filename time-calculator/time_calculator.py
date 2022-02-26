def add_minutes(start_min, duration_min):
    end_min = int(start_min) + int(duration_min)

    if end_min > 59:
        end_min -= 60
        if end_min < 10:
            return f"0{str(end_min)}", 1
        else:
            return str(end_min), 1

    if end_min < 10:
        return f"0{str(end_min)}", 0
    else:
        return str(end_min), 0

def same_period():
    if end_hours < 12: # in the same period
        return f"{str(end_hours)}:{str(end_minutes)} {period}"

def add_time(start_time, duration, starting_day=''):
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
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


    if int(start_hours) + int(duration_hours) + end_hours < 12:
        # add hours
        end_hours += int(start_hours) + int(duration_hours)
        return f"{end_hours}:{end_minutes} {period}{', ' + starting_day if starting_day else ''}"

    if int(start_hours) + int(duration_hours) + end_hours == 12:
        end_hours += int(start_hours) + int(duration_hours)
        if period == 'PM':
            new_period = 'AM'
            return f"{end_hours}:{end_minutes} {new_period} (next day)"
        else:
            new_period = 'PM'

        return f"{end_hours}:{end_minutes} {new_period}{', ' + starting_day if starting_day else ''}"

    n_days = int(int(duration_hours) / 24)
    rest_hours = int(duration_hours) % 24

    if n_days == 0:
        end_hours += int(start_hours) + int(duration_hours)
        end_hours -= 12
        if 'AM' == period:
            return f"{end_hours}:{end_minutes} {new_period}{', ' + starting_day if starting_day else ''}"

        return f"{end_hours}:{end_minutes} PM (next day)"

    if rest_hours + int(start_hours) + end_hours >= 12:
        if rest_hours + int(start_hours) + end_hours == 12:
            end_hours += int(start_hours) + rest_hours
        else:
            end_hours += int(start_hours) + rest_hours - 12
        if 'PM' == period:
            n_days += 1
            new_period = 'AM'
        else:
            new_period = 'PM'
    else:
        end_hours += int(start_hours) + rest_hours

    if starting_day:
        ending_day = days[days.index(starting_day.capitalize()) + n_days % 7]

    return f"{end_hours}:{end_minutes} {new_period}{', ' + ending_day if starting_day else ''} ({n_days} days later)"


print(add_time("8:16 PM", "466:02"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
