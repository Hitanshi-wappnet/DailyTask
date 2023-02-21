from datetime import datetime, date, timedelta

"""
6.Write a Python program to convert unix timestamp string to readable date.
"""
print(datetime.fromtimestamp(int("1284105682")).strftime("%Y-%m-%d %H:%M:%S"))


"""
7.Write a Python program to print yesterday, today, tomorrow.
"""


today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday : ", yesterday)
print("Today : ", today)
print("Tomorrow : ", tomorrow)


"""
8.Write a Python program to convert the date to datetime
(midnight of the date) in Python.
"""
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))


"""
9.Write a Python program to print next 5 days starting from today.
"""
for i in range(0, 5):
    after_five_days = date.today() + timedelta(i)
    print(after_five_days)


"""
10.Write a Python program to add 5 seconds with the current time.
"""
after_five_seconds = datetime.now() + timedelta(0, 5)
print(after_five_seconds.time())
