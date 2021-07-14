import time
import calendar

# getting current time

localtime = time.localtime(time.time())
print("local current time :", localtime)

# getting formated time

localtime = time.asctime(time.localtime(time.time()))
print('local time is', localtime)

# getting calendar of a month

cal = calendar.month(2020, 10)
print('calender is', cal)
