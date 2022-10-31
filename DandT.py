import time

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
print(time.timezone)
print(time.daylight)
print(time.tzname)