# encoding: utf-8

import random
from common.header import *
from common.sql import *
from utils.format_util import FormatUtil

class RequestDownloaderMiddleware:
    '''
    request前置处理下载中间件
    '''

    def process_request(self, request, spider): 
        try:
            # 初始化meta
            if not request.meta:
                request.meta = {}
            # url规范化
            url = request.url.replace("http://",'https://')
            # 添加请求头
            spider.make_header(request)
            # 随机user-agent
            headers_ = request.meta.get("Headers", {})
            if 'User-Agent' not in headers_ and 'user-agent' not in headers_:
                request.headers['User-Agent'] = random.sample(UA_LIST, 1)[0]

            return None
        except Exception as e:
            spider.send_log(3, "FilterDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))
