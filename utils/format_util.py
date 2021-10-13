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
    def url_md5(url):
        '''
        md5加密url
        '''
        m = hashlib.md5()
        m.update(url.encode(encoding='utf-8'))
        return m.hexdigest()