from datetime import datetime, date, timedelta
import time

"""
11.Write a Python program to convert Year/Month/Day to Day of Year in Python.
"""
today = datetime.now()
day_of_year = (today - datetime(today.year, 1, 1)).days + 1
print(day_of_year)


"""
12.Write a Python program to get current time in milliseconds in Python
"""
milli_sec = int(round(time.time() * 1000))
print(milli_sec)


"""
13.Write a Python program to get week number.
"""
print(date(2015, 6, 16).isocalendar()[1])


"""
14.Write a Python program to find the date of the first Monday of a given week.
"""
print(time.asctime(time.strptime("2015 50 1", "%Y %W %w")))


"""
15.Write a Python program to select all the Sundays of a specified year.
"""


def all_sundays(year):
    # January 1st of the given year
    dt = date(year, 1, 1)
    # First Sunday of the given year
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)


for s in all_sundays(2020):
    print(s)


"""
16.Write a Python program to add year(s) with a given date and
display the new date.
"""


def addYears(d, years):
    try:
        # Return same day of the current year
        return d.replace(year=d.year + years)
    except ValueError:
        # If not same day, it will return other
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


print("added year: ", addYears(date(2015, 1, 1), -1))


"""
17.Write a Python program to drop microseconds from datetime.
"""
dt1 = datetime.today().replace(microsecond=0)
print(dt1)


"""
18.Write a Python program to get days between two dates.
"""
a = date(2000, 3, 18)
b = date(2001, 5, 28)
print(b - a)


"""
19.Write a Python program to get the date of the last Tuesday.
"""


def latest_tuesday():
    today = date.today()
    offset = (today.weekday() - 1) % 7
    last_tuesday = today - timedelta(days=offset)
    print(last_tuesday)


latest_tuesday()


"""
20.Write a Python program to test the third Tuesday of a month.
"""


def is_third_tuesday(s):
    d = datetime.strptime(s, "%b %d, %Y")
    return d.weekday() == 1 and 14 < d.day < 22


print(is_third_tuesday("Jun 23, 2015"))
print(is_third_tuesday("Jun 16, 2015"))
