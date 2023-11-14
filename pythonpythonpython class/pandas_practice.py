#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:48:12 2023

@author: 
"""
import pandas as pd

#欄位資料
name = ['Tina', 'Sherry', 'Gary', 'Ann', 'Julia']
height = [167, 172, 178, 159, 165]

#練習一：以Series建立五位同學的身高資料，並印出內容

s = pd.Series(height, index=name)
print(s)


#練習二：1.在上面的欄位資料加入weight和age欄位資料內容
#       2.以DataFrame建立五位同學的資料，並印出內容

weight = [54, 59, 75, 45, 53]
age = [15, 17, 18, 12, 15]

df = pd.DataFrame()
df["Name"] = name
df["Height"] = height
df["Weight"] = weight
df["Age"] = age

print(df)


#練習三：將存放在DataFrame結構裡的內容輸出到csv檔案

df.to_csv("class_mate_info.csv")