# -*- coding: utf-8 -*-
import scrapy


class PoeaSpiderSpider(scrapy.Spider):
    name = 'poea_spider'
    allowed_domains = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB']
    start_urls = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB/']

    def parse(self, response):
    	agencies = body.xpath('//font[@face="Arial"]')

    	for agency in agencies: 
    		yield {
    			'Name': agency.xpath('b//text()').extract()
    			'Address': agency
    			'Telephone': 
    			'Email': 
    			'Website': 
    			'Official Rep': 
    			'Status': 
    			'License Validity': 

    		}
