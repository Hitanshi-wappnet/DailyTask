import datetime
'''
1.Write a Python script to display the various Date Time formats
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''
print("Current date and time: ", datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Current Month: ", datetime.date.today().strftime("%B"))
print("Current week number of the year:", datetime.date.today().strftime("%W"))
print("Current weekday of the week: ", datetime.date.today().strftime("%w"))
print("Current day of year: ", datetime.date.today().strftime("%j"))
print("Current day of month: ", datetime.date.today().strftime("%d"))
print("Current day of week: ", datetime.date.today().strftime("%A"))
