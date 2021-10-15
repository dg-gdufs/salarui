# encoding: utf-8

import re
import time
import hashlib
from utils.date_util import DateUtil

class FormatUtil():
    '''
    格式化工具类
    '''

    @staticmethod
    def salary_format(salary):
        l = re.findall(r'(\d*\.?\d+)-(\d*\.?\d+)(千|万)/(年|月)',salary)
        if l:
            sal = (float(l[0][0]) + float(l[0][1])) / 2.0
            if l[0][2] == '万':
                sal *= 10000
            elif l[0][2] == '千':
                sal *= 1000
            if l[0][3] == '年':
                sal /= 12.0
            return int(sal)
        raise Exception("未知salary格式:{}".format(salary))