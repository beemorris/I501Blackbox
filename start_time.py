# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 06:53:23 2018

https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

@author: Kyrie
"""

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+0, hour=7, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print("Hello world. it's "+ str(x))

t = Timer(secs, hello_world) # t = Timer(secs, webscrape_blackbox)
t.start()s