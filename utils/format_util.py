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
        return salary