# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie, becca
"""

# read in input array (through text file or with website?)
# change input each step depending on rules

import numpy as np
import os

def get_q3():
    path = '/Users/bee/Library/Mobile Documents/com~apple~CloudDocs/IU/Fall2018/I501/Blackbox/I501Blackbox/Simulation 3' #For Becca's computer
    #path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/Simulation 3 (4447 Steps)/' # for Kyrie's Laptop
    
    for file in sorted(os.listdir(path), key=lambda x: int(x.replace("_int1.txt", "").replace('sim3_step',''))): 
        if file.endswith('.txt'):
            full_matrix = np.loadtxt(path+file, delimiter=',')
            #quad1_matrix = full_matrix[0:10, 10:20]  # top right 
            quad3_matrix = full_matrix[10:20, 0:10]  # bottom left
            #quad4_matrix = full_matrix[10:20, 10:20]  # bottom right
        print(file)
        print(quad3_matrix) # Prints the quad 3 matrix for each file (might need to do something different to visualize better)

get_q3()










