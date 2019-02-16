# -*- coding: utf-8 -*-
import scrapy


class KjriSpiderSpider(scrapy.Spider):
    name = 'kjri_spider'
    allowed_domains = ['https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx']
    start_urls = ['https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx/']

    def parse(self, response):

    	table = response.xpath('//table[@class="ms-rteTable-default"]') 
    	rows = table.xpath('//tr') 

        for agencies in rows: 
        	yield {
        		'number': agencies.xpath('td//text()')[0].extract(),
        		'name': agencies.xpath('td//text()')[1].extract(),
        		'bac_expiration': agencies.xpath('td//text()')[2].extract(),
        		'address': agencies.xpath('td//text()')[3].extract(),
        		'phone': agencies.xpath('td//text()')[4].extract(),
        		'fax': agencies.xpath('td//text()')[5].extract()
        	}
