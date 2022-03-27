# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 00:05:14 2022

@author: GIGABYTE
"""

import random
sys = list() 

for i in range(6):
    num = random.randint(1,6)
    sys.append(num)
print()



    
member = list()  #串列  , 陣列
count =0

while True:
    name = int(input("請輸入號碼1~100,請輸入6次:"))
    count += 1
    member.append(name)

    if count  == 6:   
        break
    else:
        print("總共輸入",count,"次")
print()


print("系統產生號碼為:",sys)
print("-"*50)
print("您輸入的號碼為:",member) 





        