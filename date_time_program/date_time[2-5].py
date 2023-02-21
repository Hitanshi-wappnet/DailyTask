from datetime import datetime, date, timedelta

"""
2.Write a Python program to determine whether a given year is a leap year.
"""


def leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not leap year")


leap_year(2000)


"""
3.Write a Python program to convert a string to datetime.
"""


def string_to_datetime(str):
    return datetime.strptime(str, "%b %d %Y %I:%M%p")


print(string_to_datetime("Jan 1 2014 2:43PM"))


"""
4.Write a Python program to get the current time in Python.
"""
print("Current time is: ", datetime.now().time())


"""
5.Write a Python program to subtract five days from current date.
"""
dt = date.today() - timedelta(5)
print("Current Date :", date.today())
print("5 days before Current Date :", dt)
