
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 00:03:22 2023

@author: Karl_hsiao
"""

"""
 城市     土地面積（平方公里）  人口數
新北市          2053        4034102
台北市           212        2506788
桃園市          1221        2309770
台中市          2215        2839768
台南市          2192        1859728
高雄市          2952        2737582
"""

#1.Complete city_area according to the table
city_area = {'新北市':2053, 
             '台北市':212,
             '高雄市':2952 }

city_area.update({"桃園市":1221, "台中市":2215, "台南市":2192})

#2.Complete city_population according to the table
city_population = {'新北市':4034102, 
                   '高雄市':2737582 }

city_population.update({"台北市":2506788, "桃園市":2309770, "台中市":2839768, "台南市":1859728})

#3.List all cities in city_area
for i in city_area.keys():
    print(i)

#4.Finish the following query
city = input("請輸入要查詢的城市名稱：")
query = input("請輸入要查詢的欄位名稱：")

if query == '人口數':
    print(city_population.get(city))

elif query == '土地面積':
    print(city_area.get(city))


#5. Use the following dictionary structure to do the same query
list_city = [{'城市':'新北市','土地面積':2053,'人口數':4034102 },
             {'城市':'台北市','土地面積':212,'人口數':2506788 },
             {'城市':'桃園市','土地面積':1221,'人口數':2309770 },
             {'城市':'台中市','土地面積':2215,'人口數':2839768 },
             {'城市':'台南市','土地面積':2192,'人口數':1859728 },
             {'城市':'高雄市','土地面積':2952,'人口數':2737582 }
             ]

city = input("請輸入要查詢的城市名稱：")
query = input("請輸入要查詢的欄位名稱：")

for i in list_city:
    if i.get('城市') == city:
        if query == '土地面積':
            print(i.get('土地面積'))
        
        if query == '人口數':
            print(i.get('人口數'))