# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:45:23 2019

@author: mob3f
"""

import pandas as pd


data = pd.read_csv('C:/Users/mob3f/Documents/Python Scripts/EIM/App_launch_IDs.csv')

subjects=data.groupby(['EIM_id'])
results = []
last=0
i=0
for name, group in subjects:
    print(name)
    if last>0:
        last=data.timestamp
        diff=0
    else:
        diff=data.timestamp-last
    data.loc[i,].diff=diff
    i=+1
    