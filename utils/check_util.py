# encoding: utf-8

import os

class CheckUtil():
    '''
    检查工具类
    '''

    @staticmethod
    def check_path(path):
        '''
        验证路径是否存在，不存在则创建并返回。
        '''
        if not os.path.isdir(path):
            os.makedirs(path)
        return path