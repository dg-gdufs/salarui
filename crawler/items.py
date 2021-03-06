# encoding: utf-8

import scrapy


class AckItem(scrapy.Item):
    '''
    丢弃item
    '''
    res = scrapy.Field()

class OfferItem(scrapy.Item):
    offer_id = scrapy.Field()
    offer = scrapy.Field()
    category = scrapy.Field()
    area = scrapy.Field()
    salary = scrapy.Field()
    workyear = scrapy.Field()
    degree = scrapy.Field()
    date = scrapy.Field()