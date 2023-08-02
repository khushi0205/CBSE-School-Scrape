#Before running the script is is necessary that the libraries: scrapy, scrapy-proxy-tool, numpy, csv, pandas are installed, this can be done using pip install method in the terminal
#This file extracts all the links to each respective state button
#All links are saved to Links.csv
#To run the script, type "scrapy crawl CBSE" in the terminal and hit enter

import scrapy
import numpy as np
from csv import writer
from numpy import loadtxt, savetxt
import pandas as pd
import csv
class CBSESpider(scrapy.Spider):
    name = "CBSE"

    start_urls = ['https://www.cbseschool.org/']
    def parse(self, response):
        states_links = []
        states = []
        for school in response.xpath('//*[@id="states"]'):
            
                states_links = school.xpath("//*[@id='states']/div/ul/li/a/@href").extract()
                states_links.append(states_links)
                states = school.xpath("//*[@id='states']/div/ul/li/a/text()").extract()
                states.append(states)
        SL = list(states_links)
        print(SL[0])
        SL.remove(SL[-1])
        print(SL)

        from csv import writer
        from numpy import loadtxt, savetxt
        import pandas as pd
        import csv
        
        np.savetxt("Links.csv", SL, delimiter =", ", fmt ='% s')
    