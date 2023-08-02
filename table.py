#This file extracts all the required info of all the schools and is marked with "-" if the info is not provided
#All the info is saved to the csv file dedicated to the respective state
#To run the script, type "scrapy crawl Table" in the terminal and hit enter

import scrapy
import numpy as np
from csv import writer
from numpy import loadtxt, savetxt
import pandas as pd
import csv
class TableInfoSpider(scrapy.Spider):
    name = "Table"
     
    def start_requests(self):
        
        file_data = open('School_Links.csv')
        #for row in file_data:
        
        for url in file_data:
            yield scrapy.Request(url=url, callback=self.parse)  

    #start_urls = ['https://www.cbseschool.org/bharatiya-vidya-bhavan-mondal-public-school-andaman-nicobar/']
    school_info_header = []
    school_info_details = []
    state = []
    loc = []
    def parse(self, response):
        for school in response.xpath('//*[@id="responsivetable"]/table'):
            school_info_header = school.xpath('tr/td[1]//text()').extract()
            school_info_header.append(school_info_header)
            school_info_details = school.xpath('tr/td[2]//text()').extract()
            school_info_details.append(school_info_details)
            state = school.xpath('//*[@id="single-post"]/div/div/a/text()').extract()
            state.append(state)
            loc = school.xpath('//*[@id="single-post"]/div/div/p/a/text()').extract()
            loc.append(loc)



        sih = list(school_info_header)
        sih.remove(sih[-1])
        #cnt = 0
        #for i in range(len(sih)):
        #    print("SIH = ", sih)
        #    cnt +=1
        #print("Cnt= ", cnt)
            #print(school_info)
        sid = list(school_info_details)
        sid.remove(sid[-1])
        St = list(state)
        St.remove(St[-1])
        #print("St= ", St)
        Loc = list(loc)
        Loc.remove(Loc[-1])
        #print("Loc= ", Loc)
        #print(sid)

        #print("SID= ",sid)
        header = ['Name', 'Affiliate ID', 'Address', 'PIN Code', 'STD Code','Office Phone', 'Residence Phone','Fax','E-mail','Website','Foundation Year','Principal/Head of Institution','School Status','Managing Trust/Society/Committee','Location']

        for i in range(len(St)):
                for j in range(len(header)):
                    if header[j] in sih:
                        pass
                    else: 
                        sid.insert(j, "-")
        #print(sid," ", header)
                          
        

        for i in range(len(St)):
            filename = St[i] + ".csv"
            with open(filename, 'a+') as wdata:
                            csvw = writer(wdata)
                            csvw.writerow(sid + Loc)