# encoding: utf-8

import scrapy
from crawler.settings import *
from libs.mysql import Mysql
from scrapy.exceptions import CloseSpider
from crawler.items import *
from config.db_config import *
from libs.logger import Logger
from utils.format_util import FormatUtil

class BaseSpider(scrapy.Spider):
    '''
    爬虫基类，所有的爬虫都应继承自此类。
    '''

    name = 'base_spider'  # 爬虫名
    start_urls = [] # 起始网页
    proxy = '00' # 默认proxy
    mini_logger = None # 自带logger
    item_db = None # 数据库


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            # 参数设置
            for i in kwargs.keys():
                setattr(self, i, kwargs[i])
            # logger初始化
            self.mini_logger = Logger(self.name)
            # 数据库设置
            if 'crawler.pipelines.sql_pipeline.SqlPipeline' in ITEM_PIPELINES.keys():
                news_db_conf = kwargs["db"] if kwargs.get("db") in DB_CONFIG_LIST.keys() else "00"
                self.news_db = Mysql(DB_CONFIG_LIST[news_db_conf])
        except Exception as e:
            self.send_log(3, "爬虫初始化失败 ==> {}".format(e))
            raise CloseSpider('强制停止')

    def make_header(self, request):
        '''
        制作请求头，传入request中。
        request.headers[key] = value
        '''

        if "Headers" not in request.meta.keys():
            return 
        if isinstance(request.meta["Headers"], dict):
            self.send_log(2, "请求头格式错误 ==> " + str(request.meta["Headers"]))
            return 
        for key,value in request.meta["Headers"].items():
            request.headers[key] = value

    def parse(self, response):
        return AckItem()

    def send_log(self, level, log):
        '''
        批量输出log，
        level：1为info，2为warnning，3为error
        '''
        if level == 1:
            self.logger.info(log)
            self.mini_logger.info(log)
            print('INFO: {}'.format(log))
        elif level == 2:
            self.logger.warning(log)
            self.mini_logger.warning(log)
            print('WARNING: {}'.format(log))
        elif level == 3:
            self.logger.error(log)
            self.mini_logger.error(log)
            print('ERROR: {}'.format(log))