# -*- coding: utf-8 -*-
import scrapy


class JudgementSpiderSpider(scrapy.Spider):
    name = 'judgement_spider'


    allowed_domains = ['https://legalref.judiciary.hk/lrs/common/ju/ju_frame.jsp?DIS=1']
    start_urls = ['https://legalref.judiciary.hk/lrs/common/ju/ju_frame.jsp?DIS=1/']

    def parse(self, response):
        
        yield {
        	'url' : response.extract()



        }
