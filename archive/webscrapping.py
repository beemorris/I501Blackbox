# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:20:20 2018

@author: kyrie
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import requests

url = "https://www.informatics.indiana.edu/jbollen/I501F18/blackbox/BlackBox_N.php"

#browser.get(url1)
    
#url = "https://www.informatics.indiana.edu/jbollen/I501F18/blackbox/BlackBox_N.php"

#parsed = browser.page_source
#soup = BeautifulSoup(parsed,'html.parser')

soup = BeautifulSoup(requests.get(url).text, "html.parser")
#table1 = soup.find_all(class_="pty")
#toplist = []
#for row in table1:
    #.append(row.find('a').contents[0])
    
table1 = soup.find_all('table',id="system")[0]

find_step = soup.find_all('p')
current_step = float(find_step[3].contents[0][13:]) # In Numerical format

rows = table1.findChildren(['th', 'tr'])

my_table = []
my_row_index = []
my_col_index = []
i = 0
j = 0
index = []
for row in rows:
    i += 1
    cells = row.findChildren('td')
    for cell in cells:
        j += 1
        if j == 21:
            j= 1
        value = cell.string
        index.append([i,j])
        my_table.append(value)

my_table = np.reshape(my_table, (20,20))
my_table_list = my_table.tolist()

my_index = np.reshape(index, (20,20,2))
my_index_list = my_index.tolist()

# pty = 1, jfk = 2, mex = 9

