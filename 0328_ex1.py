# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 00:15:26 2022

@author: GIGABYTE
"""

import requests
import json

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=700"

bike = requests.get(url).text
data = json.loads(bike)



area = {}


for row in data:   
    if not( row["sarea"] )in area:
          area[row["sarea"]] = []        
    area[row["sarea"]].append(row["sna"])
    area[row["sarea"]].append(row["sbi"])
    area[row["sarea"]].append(row["bemp"])
    
use = input("請輸入地區:")
bikes = area.get(use)
    
if use in area:
    print(use +"所有站名,可借車輛,可停:" + str(bikes) )   
    # print( str(area[row["sbi"]])  )
    # print( str(area[row["bemp"]])  )
        

else:
    print("沒有這地區")
        

print("-"*50)


# import requests
# import json

# url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=700"

# bike = requests.get(url).text
# data = json.loads(bike)



# area = {}
# sbis = {}
# bemps = {}

# for row in data:   
#     if not( row["sarea"] )in area:
#           area[row["sarea"]] = []        
#     area[row["sarea"]].append(row["sna"])
    
    
# for row in data:     
#     if not( row["sarea"] )in sbis:
#           sbis[row["sarea"]] = []        
#     sbis[row["sarea"]].append(row["sbi"])
    
    
# for row in data:     
#     if not( row["sarea"] )in bemps:
#           bemps[row["sarea"]] = []        
#     bemps[row["sarea"]].append(row["bemp"])
    
    
    
    
# use = input("請輸入地區:")
# bikes = area.get(use)
# sbiss = sbis.get(use)
# bempss = bemps .get(use) 

    
# if use in area:
#     print(use +"所有站名:"+ str(bikes) ,end="\n",)
#     print("可借:" + str(sbiss),end="\n")
#     print("可停:" + str(bempss))


# else:
#     print("沒有這地區")
        


    
