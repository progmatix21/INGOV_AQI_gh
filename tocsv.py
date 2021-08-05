#!/usr/bin/env python
# coding: utf-8

#xml to csv converter
'''
This basic version reads a hardcoded XML filename and writes the CSV
to stdout.
'''
import xml.etree.ElementTree as ET
tree = ET.parse('data_aqi_cpcb.xml')

root = tree.getroot()

import csv
PList = ['PM2.5','PM10','NO2','NH3','SO2','CO','OZONE'] # pollutant list
print("Country,","State,","City,","Station,","PM2.5,","PM10,","NO2,","NH3,","SO2,","CO,","OZONE",sep = "")

for country in root:
    for state in country:
        for city in state:
            for station in city: # start printing the node. Next follow the data points.
                print(country.attrib['id'],state.attrib['id'],city.attrib['id'],station.attrib['id'].replace(",","")[:],sep=",",end="")
                #remove commas in station name and optionally truncate
                
                for plltnt in PList: # for each pollutant, examine dicts for entry
                    toprint = "" #default is blank
                    for entry in station.iter("Pollutant_Index"):
                        if(entry.attrib['id'] == plltnt): # entry for that pollutant exists
                            tmp_toprint = entry.attrib['Avg'] # get the Avg value; else it stays na
                            toprint = ("",tmp_toprint)[tmp_toprint.split(".")[0].isnumeric()]
                            		# False, True condition
                            break
                    
                    print(",",toprint,sep="",end="")
                print("") # a newline after each station entry





