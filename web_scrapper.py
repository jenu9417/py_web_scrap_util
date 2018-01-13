# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:22:06 2018

@author: jenu9417
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}

def scrap_page(url):
    # query the website and return the html to the variable ‘page’
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()
    
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(data, 'html.parser')
    
    print("College name : " + soup.title.string)
    
    #Explore Reviews written by
    review_blocks = soup.find_all('div', attrs={'class': 'review_blk'})
    for block in review_blocks:
        print(block.find('h4').text.strip())
        if(block.find('h4').text.strip() != "College Recommendations"):
            inner_blocks = block.find_all('div', attrs={'class':'meter_progress' })
            if (inner_blocks is None or len(inner_blocks) == 0):
               inner_blocks =  block.find_all('div', attrs={'class':'star_blk' })
            for block in inner_blocks:
               print ("\t" + block.text.strip())
        else:
            inner_blocks = block.find('div', attrs={'class':'thumb-up' })
            print("\tPosititve Recommendations " +inner_blocks.text.strip())
            inner_blocks = block.find('div', attrs={'class':'thumb-down' })
            print("\tNegative Recommendations " +inner_blocks.text.strip())
    