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
    def qcwy_salary_format(salary):
        l = re.findall(r'(\d*\.?\d+)-(\d*\.?\d+)(千|万|元)/(年|月|天)',salary)
        if l:
            sal = (float(l[0][0]) + float(l[0][1])) / 2.0
            if l[0][2] == '万':
                sal *= 10000
            elif l[0][2] == '千':
                sal *= 1000
            if l[0][3] == '年':
                sal /= 12.0
            elif l[0][3] == '天':
                sal *= 21.0
            return int(sal)
            
        l = re.findall(r'(\d*\.?\d+)(千|万|元)/(年|月|天)',salary)
        if l:
            sal = float(l[0][0])
            if l[0][1] == '万':
                sal *= 10000
            elif l[0][1] == '千':
                sal *= 1000
            if l[0][2] == '年':
                sal /= 12.0
            elif l[0][2] == '天':
                sal *= 21.0
            return int(sal)
        
        raise Exception("未知salary格式抛弃:{}".format(salary))

    def qcwy_area_format(area):
        if re.findall(r'^0(1|2|4|5|6)\d+', area):
            return '0_' + area[:2] + '0000'
        if int(area) >= 330000:
            return '0_' + area
        if re.findall(r'\d{6}', area):
            return '0_' + area[:4] + '00'
        return None
