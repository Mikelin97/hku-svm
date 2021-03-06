# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KjriScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    bac_expiration = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    fax = scrapy.Field()
