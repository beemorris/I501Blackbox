# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

# Need to annotate on plots and save to PDFs

path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/Simulation 3 (4447 Steps)/'
count = 0

for filename in sorted(os.listdir(path), key=lambda x: int(x.replace("_int1.txt", "").replace('sim3_step',''))): 
    

    if filename.endswith(".txt"):  
        count += 1
        if count < len(os.listdir(path)):
            prev = np.loadtxt(path+filename, delimiter=',')
            filename2= filename[0:9] + str(int(filename[9:-9])+1) + filename[-9:]        
            current = np.loadtxt(path+filename2, delimiter=',')
        
        '''if count ==  int(filename[9:-9]):
            prev = np.loadtxt(path+filename, delimiter=',')

            
        elif count == int(filename[9:-9])+1:   
            filename2= filename[0:9] + str(int(filename[9:-9])+1) + filename[-9:]
            current = np.loadtxt(path+filename2, delimiter=',')'''
       
           
        change = [] 
        
        #if len(prev) and len(current) > 0:
        for i in range(len(prev)): # rows
            for j in range(len(prev)): # collumns 
                if prev[i][j] != current[i][j]:
                    change.append(1)
                    
                    if i <=10 and j >=10:
                        quad = 1
                    elif i <=10 and j <=10:
                        quad = 2
                    elif i >=10 and j <=10:
                        quad = 3
                    elif i >=10 and j >=10:
                        quad = 4
                    
                    text_file = open(filename[0:4]+'.txt', 'a+')
                    text_file.write('\nStep ' + filename[9:-9] + ' to Step '+ str(int(filename[9:-9])+1))
                    text_file.write('\nIndex: (' + str(i) + ',' + str(j) + ')')
                    text_file.write('\nQuadrant: ' + str(quad) )
                    text_file.write('\nPrevious #: ' + str(prev[i][j]))
                    text_file.write('\nCurrent #: ' + str(current[i][j]))
                    text_file.write('\nDelta: ' + str(abs(prev[i][j])-current[i][j]))
                    text_file.write('\n________________________________')
                    
                else:
                    change.append(0)
        
            text_file.close()
            
        change = np.reshape(change,(20,20))
        
        fig1 = plt.figure()
        plt.imshow(change,cmap='bwr') #where 1 is red - change, blue is zero - unchanged
        plt.title('Changes from Step ' + filename[9:-9] + ' to Step '+ str(int(filename[9:-9])+1))
        
        ax = plt.gca();   

        # Major ticks
        ax.set_xticks(np.arange(.5, 20, 1));
        ax.set_yticks(np.arange(.5, 20, 1));
        
        # Labels for major ticks
        ax.set_xticklabels(np.arange(1, 20, 1));
        ax.set_yticklabels(np.arange(1, 20, 1));

        # Create offset transform by 5 points in x direction
        offset_x = matplotlib.transforms.ScaledTranslation(-5/72., 0/72., fig1.dpi_scale_trans) # dx = -5/72.; dy = 0/72.
        offset_y = matplotlib.transforms.ScaledTranslation(0/72, 5/72, fig1.dpi_scale_trans)
        
        # apply offset transform to all x ticklabels.
        for label in ax.xaxis.get_majorticklabels():
            label.set_transform(label.get_transform() + offset_x)
            
        # apply offset transform to all y ticklabels.
        for label in ax.yaxis.get_majorticklabels():
            label.set_transform(label.get_transform() + offset_y)
        
        # Gridlines based on minor ticks
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

        plt.show()




