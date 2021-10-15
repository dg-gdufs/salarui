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

            keylist = []
            valuelist = []
            for i in MYSQL_KEYS:
                if i not in item:
                    continue
                keylist.append(i)
                valuelist.append(item[i])
            spider.item_db.insert('offer', keylist, valuelist)
            spider.send_log(1, "offer抓取成功 ==> offer_id:<{}>".format(item['offer_id']))
            
            return item
        except Exception as e:
            spider.send_log(3, "SqlPipeline error ==> {} ==> item:{}".format(e, item))