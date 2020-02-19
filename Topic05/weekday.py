"""
Weekly task 5
Donal Maher

"""

import datetime
def isWeekDay():
    now = datetime.datetime.now()
    dayOfTheWeek = datetime.datetime.weekday(now)
    if dayOfTheWeek == 0 :
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 1:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 2:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 3:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 4:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 5:
        print("It is the weekend, yay!")
    elif dayOfTheWeek == 6:
        print("It is the weekend, yay!")
isWeekDay()




        



