# encoding: utf-8

from common.db_keys import *
from crawler.items import *
from common.sql import *

class SqlPipeline:
    '''
    录入SQL的Pipeline
    '''

    def process_item(self, item, spider):
        try:
            # 丢弃ack
            if isinstance(item, AckItem):
                return item

            id = spider.item_db.select(CHECK_SQL.format(item['offer_id']))
            if id:
                keylist = []
                valuelist = []
                for i in MYSQL_KEYS:
                    if i not in item:
                        continue
                    keylist.append(i)
                    valuelist.append(item[i])
                spider.item_db.update('offer', keylist, valuelist, ['id'], [id[0][0]])
                spider.send_log(1, "offer更新成功 ==> offer_id:<{}>".format(item['offer_id']))
            else:
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