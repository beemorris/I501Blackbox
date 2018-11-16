# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:57:02 2018

Blackbox Webscrape

@author: kyrie
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np


def blackbox_webscrape(sim_num, endstep,intervals):
    current_step = 1 # starting step #

    url = "https://www.informatics.indiana.edu/jbollen/I501F18/blackbox/BlackBox_N.php" # Blackbox URL
    #driver = webdriver.Chrome('C:/Users/Kyrie/GitHub/I501Blackbox/chromedriver')  # Location of chrome driver on Kyrie's Desktop
    #driver = webdriver.Chrome('C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/chromedriver')  # Location of chrome driver on Kyrie's Laptop
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver') #this is for Becca's Macbook. Comment this out and do the other drivers for Kyrie.
    
    driver.get(url) # Get URL
    
    driver.find_element_by_name("cycles").clear() # clear current interval amount
    driver.find_element_by_name("cycles").send_keys(intervals) # Set to chosen interval amount
        
    while current_step < endstep: # Run until end step 

        soup = BeautifulSoup(driver.page_source) # read page source
        
        table1 = soup.find_all('table',id="system")[0] # find blackbox table in source
        
        find_step = soup.find_all('p') # find location of current step in source
        current_step = int(find_step[3].contents[0][13:]) # Finds current step in integer format
        
        #Find all of the numbers in the 20 x 20 grid in the page source and store to my_table
        rows = table1.findChildren(['th', 'tr'])
        
        my_table = []
        i = 0
        j = 0

        for row in rows:
            i += 1
            cells = row.findChildren('td')
            for cell in cells:
                j += 1
                if j == 21: # Reset to 1 after 20
                    j= 1
                value = cell.string
                my_table.append(value)
        
        my_table2 = np.reshape(my_table, (20,20)).astype(int) # Reshape to 20 x 20 array
        
        # Save array to text file with simulation # and step # in filename
        output_file = 'sim' +str(sim_num)+ '_step' + str(current_step) + '_int' + str(intervals) + '.txt'
        np.savetxt(output_file, my_table2, delimiter=',',fmt= '%d') 
        
        # Print status
        print('Simulation ' + str(sim_num) + ': Step ' + str(current_step) + ' file saved.')
        
        time.sleep(5) # wait 5 seconds to allow for saving file
        
        # Click next button on page
        button = driver.find_element(By.XPATH, '//button[text()="Next n Step"]')
        button.click()
        
        time.sleep(5) # wait 5 seconds to wait after clicking Next Step
        

# Initiates the blackbox function (can tweak the inputs of simulation number, end step and the intervals)            
blackbox_webscrape(3, 7000, 1)    # blackbox_webscrape(sim_num, endstep,intervals)          
            
            
            
            
            
            
            
            
            


