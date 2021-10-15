# encoding: utf-8

from config.settings_config import *
from config.host_config import *
from utils.date_util import DateUtil
from utils.check_util import CheckUtil

BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

LOG_LEVEL = LOG_DEFAULT_LEVEL # 日志输出等级
LOG_FILE = CheckUtil.check_path(LOG_DEFAULT_HOME) + '/default[{}].txt'.format(DateUtil.time_now_formate().split(' ')[0]) # 日志默认输出

RETRY_ENABLED = True # 开启重试
RETRY_TIMES = 3  # 重试3次
RETRY_HTTP_CODES = [429, 500, 502, 503, 504, 522, 524, 408, 301, 302, 414, 400, 403, 418, 419]  # 重试的情况
HTTPERROR_ALLOWED_CODES = []  # 允许进入Spider的情况
DOWNLOAD_TIMEOUT = 30  # 30秒超时
# DOWNLOAD_DELAY = 0.2 # 0.2秒间隔

EXTENSIONS = BASE_EXTENSIONS # 扩展件
DOWNLOADER_MIDDLEWARES = BASE_DOWNLOADER_MIDDLEWARES # 下载中间件
ITEM_PIPELINES = BASE_ITEM_PIPELINES # 管道
SPIDER_MIDDLEWARES = BASE_SPIDER_MIDDLEWARES # 爬虫中间件

DEFAULT_REQUEST_HEADERS = BASE_DEFAULT_REQUEST_HEADERS # 默认请求头