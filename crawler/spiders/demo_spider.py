# encoding: utf-8

from crawler.spiders import BaseSpider
from crawler.items import *
from utils.date_util import DateUtil
from scrapy.http.request import Request

class DemoSpiderSpider(BaseSpider):
    name = 'demo_spider'
    start_urls = ['https://www.baidu.com/']
