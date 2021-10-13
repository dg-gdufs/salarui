# encoding: utf-8

from utils.date_util import *
from config.host_config import *

class Logger():
        
        file = None

        # 初始化logger
        def __init__(self, name):
                time_now = DateUtil.time_now_formate().replace(':',';')
                self.file = open(LOG_DEFAULT_HOME + '/{}[{}].txt'.format(name, time_now), 'a', encoding='utf-8')

        def info(self, log):
                '''
                info消息
                '''
                time_now = DateUtil.time_now_formate()
                self.file.write('INFO [{}] : {}\n'.format(time_now, log))
                self.file.flush()

        def warning(self, log):
                '''
                warning消息
                '''
                time_now = DateUtil.time_now_formate()
                self.file.write('WARNING [{}] : {}\n'.format(time_now, log))
                self.file.flush()

        def error(self, log):
                '''
                error消息
                '''
                time_now = DateUtil.time_now_formate()
                self.file.write('ERROR [{}] : {}\n'.format(time_now, log))
                self.file.flush()