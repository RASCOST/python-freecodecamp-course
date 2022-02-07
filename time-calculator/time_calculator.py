def add_time(start_time, duration, starting_day=''):
    end_minutes = 0
    end_hours = 0

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
    #end_hours += start_hours + duration_hours
    return f"{str(end_hours)}:{str(end_minutes)}"

print(add_time("3:55 PM", "3:15"))
