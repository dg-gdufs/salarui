# encoding: utf-8

from config.host_config import *

class ProxyDownloaderMiddleware:
    '''
    proxy下载中间件
    '''

    # 设置代理
    def process_request(self, request, spider): 
        try:
            if request.meta == None:
                request.meta = {}
            request.meta['proxy'] = PROXY_HOST_LIST[spider.proxy]
            return None
        except Exception as e:
            spider.send_log(3, "ProxyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))