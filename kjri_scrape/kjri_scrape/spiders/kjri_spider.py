# -*- coding: utf-8 -*-
import scrapy


class KjriSpiderSpider(scrapy.Spider):
    name = 'kjri_spider'
    allowed_domains = ['https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx']
    start_urls = ['http://https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx/']

    def parse(self, response):
        pass
