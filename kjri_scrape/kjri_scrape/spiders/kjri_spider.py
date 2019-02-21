# -*- coding: utf-8 -*-
import scrapy
from kjri_scrape.items import KjriScrapeItem 


class KjriSpiderSpider(scrapy.Spider):
    name = 'kjri_spider'
    allowed_domains = ['https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx']
    start_urls = ['https://www.kemlu.go.id/hongkong/id/layanan-konsuler/Pages/agencies.aspx/']

    def parse(self, response):


    	table = response.xpath('//table[@class="ms-rteTable-default"]') 
    	rows = table.xpath('//tr') 
    	item_list = []

        for agencies in rows:
        	agency_item = KjriScrapeItem() 
        	agency_item['number'] = agencies.xpath('td//text()')[0].extract()
        	agency_item['name'] = agencies.xpath('td//text()')[1].extract()
        	agency_item['bac_expiration'] = agencies.xpath('td//text()')[2].extract()
        	agency_item['address'] = agencies.xpath('td//text()')[3].extract()
        	agency_item['phone'] = agencies.xpath('td//text()')[4].extract()
        	agency_item['fax'] = agencies.xpath('td//text()')[5].extract()

        	item_list.append(agency_item) 

        return item_list



	        # yield {
	        # 		'product_key': temp.items()
	        # 		# 'name': ,
	        # 		# 'bac_expiration': ,
	        # 		# 'address': ,
	        # 		# 'phone': ,
	        # 		# 'fax': 
	        # 	}
	