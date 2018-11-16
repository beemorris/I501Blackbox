# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie

@editor: Becca
"""

# read in input array (through text file or with website?)
# change input each step depending on rules

import numpy as np
import os

def get_q3():
	path = '/Users/bee/Library/Mobile Documents/com~apple~CloudDocs/IU/Fall2018/I501/Blackbox/I501Blackbox/'

	for filename in os.listdir(path):
		if filename.endswith('_int1.txt'):
			full_matrix = np.loadtxt(filename, delimiter=',')
			quad1_matrix = full_matrix[0:10, 10:20]  # top right
			quad2_matrix = full_matrix[0:10, 0:10]  # top left
			quad3_matrix = full_matrix[10:20, 0:10]  # bottom left
			quad4_matrix = full_matrix[10:20, 10:20]  # bottom right
	print(quad3_matrix)


get_q3()
#get_input_data('C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/archive/test 3/sim1_step1_int1.txt')









