# encoding: utf-8

import time
from common.date import *

class DateUtil():
    '''
    时间工具类
    '''

    @staticmethod
    def time_now_formate():
        '''
        返回当前的格式化时间，格式：%Y-%m-%d %H:%M:%S
        '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def formate_time2time_stamp(time_):
        '''
        将传入的格式化时间转为时间戳，格式：%Y-%m-%d %H:%M:%S
        '''
        return int(time.mktime(time.strptime(time_, "%Y-%m-%d %H:%M:%S")))

    @staticmethod
    def time_stamp2formate_time(time_):
        '''
        将传入的时间戳转为格式化时间，格式：%Y-%m-%d %H:%M:%S
        '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time_)))

    @staticmethod
    def time_ago(year=0, month=0, week=0, day=0, hour=0, minute=0, second=0):
        '''
        返回指定时间之前的时间戳
        '''
        stamp = int(time.time()) - second - minute*60 - hour*3600 - day*86400 - week*604800 - month*2592000 - year*31536000
        return (stamp if stamp > 0 else 0)
