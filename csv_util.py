# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:14:04 2018

@author: jenu9417
"""

import csv

############################# CSV Reader #####################################    

class CSV_Reader:
    
    def __init__(self,file):
        self.file = file
        
    def readCSV(self):
        response = Response()
        header_list = []
        data_list = []
        file = open(self.file)
        reader = csv.reader(file)
        
        rownum = 0
        for row in reader:
            if rownum == 0:
                header_list = row
            else:
                colnum = 0
                data = {}
                for col in row:
                    data[header_list[colnum]]=col
                    colnum += 1
                
                data_list.append(data)
            
            rownum += 1
        
        response.header_list = header_list
        response.data_list = data_list
        
        return response

############################# CSV Writer #####################################    

class CSV_Writer:
    
    def __init__(self,file):
        self.file = file
        
    def writeCSV(self, response):
        if isinstance(response, Response):
            file = open(self.file,'w',newline='')
            writer = csv.DictWriter(file, fieldnames=response.header_list)
            
            writer.writeheader();
            writer.writerows(response.data_list)
        else:
            print('Invalid Input !!')

############################# Response ######################################   
            
class Response:
    header_list = []
    data_list = []
    
    def __str__(self):
        return 'Header_List : {0}\n\nData_List : {1}'.format(self.header_list, self.data_list)