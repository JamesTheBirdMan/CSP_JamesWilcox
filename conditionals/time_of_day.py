# James Wilcox, Time of Day Python

import time
# first instance of time
#print(time.gmtime(0))

#time in seconds since gmtime
current = time.time()

#current time as we are used to seeing it
now = time.ctime(current)
print(now)

#get just the hour
local_time = time.localtime(current)
hour = local_time.tm_hour
#print(hour)

if hour >= 6 and hour <= 11:
    print("Good Morning!")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon!")
elif hour >=17 and hour <= 19:
    print("Good Evening")
else:
    print(f"You should be in bed!")