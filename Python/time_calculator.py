def convert_time_24(time_with_unit):
    time, time_unit = time_with_unit.split()
    hours, mins = time.split(":")

    if time_unit == "AM":
        if hours == "12":
            return "00:" + mins
        else:
            return time
    if time_unit == "PM":
        if hours == "12":
            return "12:" + mins
        else:
            time_converted = 12 + int(hours)
            return str(time_converted) + ":" + mins


def convert_time_12(time_without_unit):
    hours, mins = time_without_unit.split(":")
    hours = int(hours)

    if hours == 0:
        return "12:" + str(mins) + " AM"
    if hours < 12:
        return time_without_unit + " AM"
    if hours == 12:
        return time_without_unit + " PM"
    if hours > 12:
        converted_time = hours - 12
        return str(converted_time) + ":" + mins + " PM"


def weekday_calc(days_extra, b):
    if not b:
        return ""
    if days_extra == 0:
        return ", " + b

    week = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]
    b = b.lower()
    index = week.index(b)
    if index + days_extra > 6:
        weekday = (index + days_extra) % 7
        output = week[weekday]
    else:
        output = week[index + days_extra]
    return ", " + output.capitalize()


def add_time(start, duration, b=""):
    start_24 = convert_time_24(start)
    hours, mins = start_24.split(":")
    duration_hours, duration_mins = duration.split(":")

    hours = int(hours)
    mins = int(mins)
    duration_mins = int(duration_mins)
    duration_hours = int(duration_hours)
    mins_added = mins + duration_mins

    hours_extra = int(mins_added / 60)
    rest_mins = mins_added % 60

    hours_added = hours + duration_hours + hours_extra

    days_extra = int(hours_added / 24)
    rest_hours = hours_added % 24

    time_joined = str(rest_hours) + ":" + str(rest_mins).zfill(2)

    convert_back = convert_time_12(time_joined)

    weekday = weekday_calc(days_extra, b)

    if days_extra == 0:
        last_part = ""
    elif days_extra == 1:
        last_part = " (next day)"
    else:
        last_part = " (" + str(days_extra) + " days later)"

    return (convert_back + weekday + last_part)
