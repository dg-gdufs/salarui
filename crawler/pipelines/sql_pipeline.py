# encoding: utf-8

import json
from utils.date_util import DateUtil
from utils.format_util import FormatUtil
from common.db_keys import *
from crawler.items import *

class SqlPipeline:
    '''
    录入SQL的Pipeline
    '''

    def process_item(self, item, spider):
        try:
            # 丢弃ack
            if isinstance(item, AckItem):
                return item

            '''
            在此填写逻辑
            '''

            spider.send_log(1, "网页抓取成功 ==> url:<{}>".format(''))
            return item
        except Exception as e:
            spider.send_log(3, "SqlPipeline error ==> {} ==> item:{}".format(e, item))