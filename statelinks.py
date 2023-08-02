#This file extracts all the links to the school web page that contains info of the schools present in the state 
#All links are saved to School_Links.csv
#To run the script, type "scrapy crawl StLinks" in the terminal and hit enter


import scrapy
import numpy as np
from csv import writer
from numpy import loadtxt, savetxt
import pandas as pd
import csv
class CBSESLSpider(scrapy.Spider):
    name = "StLinks"
    
    file_data = open('Links.csv')

    def start_requests(self):
        file_data = open('Links.csv')
        #for row in file_data:
       
        for url in file_data:
            yield scrapy.Request(url=url, callback=self.parse)
            


    school_links = []
    def parse(self, response):
        for school in response.xpath('//*[@id="blog"]'):
            school_links = school.xpath("//*[@id='blog']/div/div/h2/a/@href").extract()
            school_links.append(school_links)
            #print(school_links)
        sl = list(school_links)
        sl.remove(sl[-1])
        #print(sl)
        with open('School_Links.csv','a') as csvfile:
            np.savetxt(csvfile, sl ,delimiter=',',fmt='%s')
        next_page = response.xpath("//*[@id='blog']/div[1]/div[61]/a[3]/@href").extract()
        #print(next_page[0])
        if next_page[0] is not None:
            yield scrapy.Request(url=next_page[0], callback=self.parse)            