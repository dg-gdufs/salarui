# encoding: utf-8

import scrapy


class AckItem(scrapy.Item):
    '''
    丢弃item
    '''
    res = scrapy.Field()
