# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:25:18 2018

@author: kyrie
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Lord of the Rings')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()