# -*- coding: utf-8 -*-
import scrapy
from poea_scrape.items import PoeaScrapeItem

class PoeaSpiderSpider(scrapy.Spider):
    name = 'poea_spider'
    allowed_domains = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB']
    start_urls = ['http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB/']

    def parse(self, response):
    	agencies = response.xpath('//font[@face="Arial"]')


        agency_output = []

    	for agency in agencies: 
            poea_item = PoeaScrapeItem() 
            poea_item['name'] = agency.xpath('b//text()').extract()
            poea_item['address'] = agency.re_first(r'<br>(.*?)<br>')
            poea_item['telephone'] = agency.re(r'Tel No/s</em> : \&amp;nbsp(.*?)\&')
            poea_item['email'] = agency.re(r'Email Address</em> : \&amp;nbsp(.*?)<br>')
            poea_item['website'] = agency.re(r'Website</em> : \&amp;nbsp(.*?)<br>')
            poea_item['official_rep'] = agency.re(r'Official Representative</em> : (.*?)<br>')
            poea_item['status'] = agency.re(r'Status</em> : (.*?)<br>')
            poea_item['license_validity'] = agency.re(r'License Validity</em> : (.*?)<br>')
            agency_output.append(poea_item)

        return agency_output

    		# yield {
    		# 	'Name': agency.xpath('b//text()').extract(), 
    		# 	'Address': agency.re_first(r'<br>(.*?)<br>'), 
    		# 	'Telephone': agency.re(r'Tel No/s</em> : \&amp;nbsp(.*?)\&'),
    		# 	'Email': agency.re(r'Email Address</em> : \&amp;nbsp(.*?)<br>'),
    		# 	'Website': agency.re(r'Website</em> : \&amp;nbsp(.*?)<br>'),
    		# 	'Official Rep': agency.re(r'Official Representative</em> : (.*?)<br>'),
    		# 	'Status': agency.re(r'Status</em> : (.*?)<br>'),
    		# 	'License Validity': agency.re(r'License Validity</em> : (.*?)<br>')
    		# }

