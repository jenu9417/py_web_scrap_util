# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 21:43:49 2018

@author: jenu9417
"""
# import libraries
import csv_util
import sys
import time
import web_scrapper

# Read input csv file and fetch url link
csv_reader = csv_util.CSV_Reader(sys.argv[0])
response = csv_reader.readCSV();
data_list = response.data_list;

print("Starting web scraping util...")

for data in data_list:
   try:
       web_scrapper.scrap_page(data['Link'])
       #explicit timeout for bypassing anti-bot measures
       time.sleep(2)
   
   except:
       print('Error occured for : ' + data['Link'])


#provide consolidated disctionary list to data for exporting response as csv
data = { "fruit" : "apple" }
csv_writer = csv_util.CSV_Writer('response.csv')
csv_writer.writeCSV(data);      