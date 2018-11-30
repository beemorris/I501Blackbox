# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:18:25 2018

@author: kyrie
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Potential future add: create 2 other subplots of original color grids?

def plot_num_changes(path,sim):
    count = 0
    fig1 = []
    
    for filename in sorted(os.listdir(path), key=lambda x: int(x.replace("_int1.txt", "").replace('sim'+str(sim)+'_step',''))): 
        
        if filename.endswith(".txt"):  
            count += 1
            if count < len(os.listdir(path)):
                prev = np.loadtxt(path+filename, delimiter=',')
                filename2= filename[0:9] + str(int(filename[9:-9])+1) + filename[-9:]        
                current = np.loadtxt(path+filename2, delimiter=',')
           
            info = []   
            change = [] 
            
            for i in range(len(prev)): # rows
                for j in range(len(prev)): # collumns 
                    if prev[i][j] != current[i][j]:
                        change.append(1)
                        
                        if i <=9 and j >=10:
                            quad = 1
                        elif i <=9 and j <=9:
                            quad = 2
                        elif i >=10 and j <=9:
                            quad = 3
                        elif i >=10 and j >=10:
                            quad = 4
                        
                        text_file = open(filename[0:4]+'.txt', 'a+')
                        
                        line1 = '\nStep ' + filename[9:-9] + ' to Step '+ str(int(filename[9:-9])+1)
                        line2 = '\nIndex: (' + str(i) + ',' + str(j) + ')'
                        line3 = '\nQuadrant: ' + str(quad)
                        line4 = '\nPrevious #: ' + str(prev[i][j])
                        line5 = '\nCurrent #: ' + str(current[i][j])
                        line6 = '\nDelta: ' + str(abs(prev[i][j])-current[i][j])
                        line7 = '\n______________'
                        
                        text_file.write(line1)
                        text_file.write(line2)
                        text_file.write(line3)
                        text_file.write(line4)
                        text_file.write(line5)
                        text_file.write(line6)
                        text_file.write(line7)
                        
                        info.append(line2+line3+line4+line5+line6+line7)
                        
                        text_file.close()
                        
                    else:
                        change.append(0)
            
                
            change = np.reshape(change,(20,20))
            
            fig1.append(plt.figure())
            #font = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 16,}
            plt.imshow(change,cmap='bwr') #where 1 is red - change, blue is zero - unchanged
            plt.title('Changes from Step ' + filename[9:-9] + ' to Step '+ str(int(filename[9:-9])+1)) #, fontdict=font
                        
            ax = plt.gca();  
            
            # Gridlines based on minor ticks
            ax.grid(which='major', color='grey', linestyle='-', linewidth=1.5)
            
            # Annotate Index Info and Changes between Steps to the Right of Grid
            trans = ax.get_xaxis_transform() 
            ax.annotate(''.join(info), xy=(21, -.2), xycoords=trans)
    
            # Major ticks
            ax.set_xticks(np.arange(.5, 20, 1));
            ax.set_yticks(np.arange(.5, 20, 1));
            
            # Labels for major ticks
            ax.set_xticklabels(np.arange(0, 19, 1));
            ax.set_yticklabels(np.arange(0, 19, 1));
    
            # Create offset transform by 5 points in x and y direction
            offset_x = matplotlib.transforms.ScaledTranslation(-5/72., 0/72., fig1[count-1].dpi_scale_trans) # dx = -5/72.; dy = 0/72.
            offset_y = matplotlib.transforms.ScaledTranslation(0/72, 5/72, fig1[count-1].dpi_scale_trans)
            
            # Apply offset transform to all x ticklabels (so that x-axis #s line up with boxes)
            for label in ax.xaxis.get_majorticklabels():
                label.set_transform(label.get_transform() + offset_x)
                
            # Apply offset transform to all y ticklabels (so that y-axis #s line up with boxes)
            for label in ax.yaxis.get_majorticklabels():
                label.set_transform(label.get_transform() + offset_y)

            # Separate Quadrants
            ax.axhline(y=9.5,color='w')
            ax.axvline(x=9.5,color='w')
            
            # Show Plot
            plt.show()
            
    return fig1

# Modify Directory path and Simulation # 
#path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/archive/test 3/' # short file test
    
#path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/Simulation 3 (4447 Steps)/'
#sim = 3 # 1

path = 'C:/Users/kyrie/OneDrive/Documents/GitHub/I501Blackbox/Simulation 7 (6484 Steps)/'
sim = 7 # 1

# Run the Program and get figure information for PDF 
f1 = plot_num_changes(path,sim)  

# Create PDF File
pp = PdfPages('sim'+str(sim)+'_num_change_plots.pdf')

# Save all of the figures to PDF
for elem in range(len(f1)-1):
    pp.savefig(f1[elem], dpi=72)
    
# Close PDF (Will not open properly if code doesn't close out at the end)    
pp.close() 

print('Huzzah! The code finished running! Have a rainbow cookie you special unicorn!')
