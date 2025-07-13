#!/usr/bin/env python3
# Student ID: Sing Man Wong
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour,minute,second):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    while sum.second >= 60: # while sum.second >= 60:
        sum.second = sum.second - 60 # minus 60 second for 1 minute
        sum.minute = sum.minute + 1 # increase 1 minute
    while sum.minute >= 60: # while sum.minute >= 60:
        sum.minute = sum.minute - 60 # minus 60 minute for 1 hour
        sum.hour = sum.hour + 1 # increase 1 hour
    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1
        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1
        while time.second < 0: # While the second < 0
            time.second += 60 # add back 60 seconds for it
            time.minute -=1 # but minus 1 in minute
        while time.minute < 0: # while the minute < 0
            time.minute += 60 # add back 60 minutes for it
            time.hour -=1 # but minus 1 in hour
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
