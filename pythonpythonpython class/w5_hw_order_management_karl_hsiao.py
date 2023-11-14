#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:54:20 2023

@author: selinayen
"""

order = [ '編號', '品名', 0, 0, 0 ]

menu = """
1. 修改訂單號碼
2. 修改品名
3. 修改單價
4. 修改數量
5. 查詢訂單金額
請輸入選項1-5，或Q/q離開：
"""

while True:
    ans = input(menu)
    if ans == 'q' or ans == 'Q':
        break
    else:
        if ans == '1':
            order[0] = input("請輸入要修改的訂單號碼：")
        elif ans == "2":
            order[1] = input("請輸入要修改的品名：")
        elif ans == "3":
            order[2] = int(input("請輸入要修改的單價："))
        elif ans == "4":
            order[3] = int(input("請輸入要修改的數量："))
        elif ans == "5":
            print("訂單金額為：", order[4])

    order[4] = order[3] * order[2]