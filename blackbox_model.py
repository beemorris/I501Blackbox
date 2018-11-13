# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie
"""

# read in input array (through text file or with website?)
# change input each step depending on rules

import numpy as np

def get_input_data(start_file):

    full_matrix = np.loadtxt(start_file, delimiter=',')

    quad1_matrix = full_matrix[0:10,10:20] # top right
    quad2_matrix = full_matrix[0:10,0:10] # top left
    quad3_matrix = full_matrix[10:20,0:10] # bottom left
    quad4_matrix = full_matrix[10:20,10:20] # bottom right
    
    #If want in list form just add .tolist()
    
    #MANIPULATE DATA WITH RULES

    # If need to get interval value
    #input_step = driver.find_element_by_name("cycles") #find the textbox of input step
    #intervals = int(input_step.get_attribute('value')) # get value from that box in integer format (could be coded to change later)
        
get_input_data('C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/archive/test 3/sim1_step1_int1.txt')