#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:20:45 2023

@author: Karl_hsiao
"""

#1.建立一個內容含有 'apple', 'cherry', 'banana' 的 Tuple 物件 T1
T1 = ("apple", "cherry", "banana")
 
#2.建立一個空 的 Tuple 物件 T2
T2 = ()

#3.輸出 T1 物件裡有幾個項目
print(len(T1))

#4.檢查 'apple' 是否在 T1 裡，是的話，輸出 'Yes'
if "apple" in T1:
    print("Yes")

#5.輸出 T1 內容, 並在後面加註字串長度，例：apple(5), cherry(6), banana(6)
for i in T1:
    print(i+f"({len(i)})")