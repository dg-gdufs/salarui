# encoding: utf-8

from scrapy import signals

class LogExtension:
    '''
    logger extension的处理
    '''

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_error, signal=signals.spider_error)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    # 错误日志输出
    def spider_error(self, failure, response, spider):
        spider.send_log(3, 'spider error ==> {} ==> url:<{}>'.format(failure.value, response.url))
        spider.mini_logger.error(failure)

    # 爬虫关闭日志输出
    def spider_closed(self, spider, reason):
        spider.mini_logger.info('爬虫结果 ==> ' + str(spider.crawler.stats.get_stats()))
