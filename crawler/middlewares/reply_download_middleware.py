# encoding: utf-8

from scrapy.exceptions import IgnoreRequest
from scrapy.downloadermiddlewares.retry import RetryMiddleware

class ReplyDownloaderMiddleware:
    '''
    reply下载中间件
    '''

    def process_response(self, request, response, spider):
        try:
            if response.status >= 300 or response.status <200:
                spider.send_log(2, "状态码错误 ==> status:{} ==> url:<{}>".format(response.status, response.url))
            return response
        except Exception as e:
            spider.send_log(3, "ReplyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, response.url))

    def process_exception(self, request, exception, spider):
        if isinstance(exception, RetryMiddleware.EXCEPTIONS_TO_RETRY):
            spider.send_log(3, 'downloader error ==> ({}) ==> url:<{}>'.format(exception, request.url))