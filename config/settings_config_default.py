# encoding: utf-8

"""
Scrapy默认中间件
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
"""

# 日志等级，默认INFO就可
LOG_DEFAULT_LEVEL = "INFO"

# 默认请求头，可以更改此项用于测试
BASE_DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

# 以下四个为各类插件，可以根据自己需求删除或添加用于测试
BASE_EXTENSIONS = {
    'crawler.extensions.log_extension.LogExtension': 500,
}

BASE_DOWNLOADER_MIDDLEWARES = {
    'crawler.middlewares.request_download_middleware.RequestDownloaderMiddleware': 543,
    'crawler.middlewares.proxy_download_middleware.ProxyDownloaderMiddleware': 544,
    'crawler.middlewares.reply_download_middleware.ReplyDownloaderMiddleware': 551,
}

BASE_ITEM_PIPELINES = {
    # 'crawler.pipelines.sql_pipeline.SqlPipeline': 300,
}

BASE_SPIDER_MIDDLEWARES = {}