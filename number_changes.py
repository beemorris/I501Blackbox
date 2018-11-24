# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie
"""

import numpy as np
import matplotlib.pyplot as plt
import os


path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/Simulation 3 (4447 Steps)/'
count = 0
#prev = [] 
#current = []

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
                    
                    text_file = open(filename[0:4]+'.txt', 'w')
                    text_file.write('Step ' + filename[9:-9] + ' to Step '+ str(int(filename[9:-9])+1))
                    text_file.write('Index: (' + str(i) + ',' + str(j) + ')')
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
        
        ax = plt.gca();   

        # Major ticks
        ax.set_xticks(np.arange(0, 20, 1));
        ax.set_yticks(np.arange(0, 20, 1));
        
        # Labels for major ticks
        ax.set_xticklabels(np.arange(1, 20, 1));
        ax.set_yticklabels(np.arange(1, 20, 1));

        
        # Minor ticks
        ax.set_xticks(np.arange(-.5, 20, 1), minor=True);
        ax.set_yticks(np.arange(-.5, 20, 1), minor=True);
        
        # Gridlines based on minor ticks
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

        plt.show()

        
'''
data = np.random.rand(10, 10) * 20

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [0,10,20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 10, 1));
ax.set_yticks(np.arange(-.5, 10, 1));

plt.show()'''



