# -*- coding: utf-8 -*-
import scrapy


class PoeaSpiderSpider(scrapy.Spider):
    name = 'poea_spider'
    allowed_domains = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB']
    start_urls = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB/']

    def parse(self, response):
    	agencies = response.xpath('//font[@face="Arial"]')
        agency_info = agencies.re_first(r'<br>(.*?)<br>')

    	for agency in agencies: 
    		yield {
    			'Name': agency.xpath('b//text()').extract(),
    			'Address': agency_info,
    			'Telephone': agency.re(r'Tel No/s</em> : \&amp;nbsp(.*?)\&'),
    			'Email': agency.re(r'Email Address</em> : \&amp;nbsp(.*?)<br>'),
    			'Website': agency.re(r'Website</em> : \&amp;nbsp(.*?)<br>'),
    			'Official Rep': agency.re(r'Official Representative</em> : (.*?)<br>'),
    			'Status': agency.re(r'Status</em> : (.*?)<br>'),
    			'License Validity': agency.re(r'License Validity</em> : (.*?)<br>')
    		}
