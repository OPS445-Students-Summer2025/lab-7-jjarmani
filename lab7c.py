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
    # sum = Time(0,0,0)
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second

    # while sum.second >= 60: # while sum.second >= 60:
    #     sum.second = sum.second - 60 # minus 60 second for 1 minute
    #     sum.minute = sum.minute + 1 # increase 1 minute
    # while sum.minute >= 60: # while sum.minute >= 60:
    #     sum.minute = sum.minute - 60 # minus 60 minute for 1 hour
    #     sum.hour = sum.hour + 1 # increase 1 hour
    # return sum

    tot_second = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(tot_second) # using sec_to_time function

def change_time(time, seconds):
    # time.second += seconds
    # if valid_time(time) != True:
    #     while time.second >= 60:
    #          time.second -= 60
    #          time.minute +=1
    #     while time.minute >= 60:
    #          time.minute -= 60
    #          time.hour += 1
    #     while time.second < 0:
    #         time.second += 60
    #         time.minute -=1
    #     while time.minute < 0:
    #         time.minute += 60
    #         time.hour -=1
    # return None

    tot_second = time_to_sec(time) + seconds # using time_to_sec function
    if tot_second > 0: # if the total amount of second is > 0
        new_time = sec_to_time(tot_second) # store in new_time variable using sec_to_time function (that will convert to proper format)
        time.hour = new_time.hour
        time.minute = new_time.minute
        time.second = new_time.second
    return None

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time(0,0,0)
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
