#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:50:34 2023

@author: your name
"""

"""
Define a function to read city information from file
This function will return a list of dictionaries that contain city information
"""
#1. Put your code here
try:
    with open("file.txt", "x") as f:

        file = "新北市    2053    4034102\n台北市     212    2506788\n桃園市    1221    2309770\n台中市    2215    2839768\n台南市    2192    1859728\n高雄市    2952    2737582"
        f.write(file)

except:
    with open("file.txt", "w") as f:

        file = "新北市    2053    4034102\n台北市     212    2506788\n桃園市    1221    2309770\n台中市    2215    2839768\n台南市    2192    1859728\n高雄市    2952    2737582"
        f.write(file)


with open("file.txt", "r") as f:

    print(f.read())



#city_list = read_from_file('city_information.txt')

"""
Display city information on screen as following
新北市    2053    4034102
台北市     212    2506788
桃園市    1221    2309770
台中市    2215    2839768
台南市    2192    1859728
高雄市    2952    2737582
"""

#2. Put your code here