# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoeaScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    website = scrapy.Field() 
    status = scrapy.Field() 
    address = scrapy.Field() 
    telephone = scrapy.Field() 
    email = scrapy.Field() 
    license_validity = scrapy.Field() 
    official_rep = scrapy.Field() 

