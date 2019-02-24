# -*- coding: UTF-8 -*-
import re
from time import sleep
import requests
from fake_useragent import UserAgent
ua = UserAgent()
import urllib2
import html2text

i = 0
base = "https://legalref.judiciary.hk/lrs/common/ju/ju_body.jsp?DIS="
session = requests.Session()
session.headers.update({'User-Agent': ua.random})

def get_judgements(current_number): 
    while True:
        url = base + str(current_number)
        print(url)
        try: 
            response = session.get(url, timeout=3)
            page = urllib2.urlopen(url, timeout=3)
        #print response.content
        except urllib2.URLError, error: 
            print("catch Exception",error)
            return
            
            #return current_number
        #check if there is a timeout 

        
        try: 
            html_content = page.read()
        except: 
            print("What happened?")
        file = open(str(current_number)+'-HK-Judiciary.txt', 'w')
        file.write(html_content)
        file.close()
        sleep(0.01)

        current_number = current_number + 1



 