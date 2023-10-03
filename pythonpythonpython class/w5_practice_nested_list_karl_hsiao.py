#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:48:53 2023

@author: Karl_hsiao
"""

#訂單
order = ['0001']
total = 0

#購物明細
items = [['蘋果', 50, 2],
         ['香蕉', 60, 1],
         ['葡萄', 100, 1]]

#計算總金額

for i in items:
    total += i[1] * i[2]

order.append(items)
order.append(total)

#把「購物明細」和「總金額」加到 order 裡
#讓 print(order) 得到 [ '0001', [['蘋果', 50, 2],['香蕉', 60, 1],['葡萄', 100, 1]], 總金額 ]
print(order)
