# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:45:23 2019

@author: mob3f
"""

import pandas as pd
from datetime import datetime


data = pd.read_csv('C:/Users/mehdi/Documents/Python Scripts/EIM/App_launch_IDs.csv')
data = data[data.event_type != 'recruitment_opt_out']

subjects=data.groupby(['EIM_id','package'])
results = []
data.event_type.unique()
data["diff"]=0

for name, group in subjects:
    print(name)
    last=0
    duration=0
    group=group.sort_values(by='timestamp')
    for index,frame in group.iterrows():
        if last==0:
            diff=1
        else:  
            diff=frame.timestamp-last
            if diff>60:
                results.append({'EIM_id':name[0],'timestamp': frame.timestamp-duration, 'Duration': duration, 'package':name[1], 'date':datetime.utcfromtimestamp(frame.timestamp).strftime('%Y-%m-%d %H:%M:%S')})
                duration=0
            elif diff<0:
                print('time '+ str(frame.timestamp)+'  last  '+str(last))
            else:
                duration=duration+diff
        last=frame.timestamp

clean=pd.DataFrame(results)
clean.to_csv('C:/Users/mehdi/Documents/Python Scripts/EIM/App_launch_IDs_clean.csv')

stat=clean[['EIM_id','Duration','package']].groupby(['EIM_id']).agg(['mean', 'count','sum','max','min','std'])
stat.to_csv('C:/Users/mehdi/Documents/Python Scripts/EIM/App_launch_IDs_stats_user.csv')

stat=clean[['EIM_id','Duration','package']].groupby(['package']).agg(['mean', 'count','sum','max','min','std'])
stat.to_csv('C:/Users/mehdi/Documents/Python Scripts/EIM/App_launch_IDs_stats_package.csv')


clean["Duration"].hist(alpha=0.5,column='diff',bins=10)


data["diff"]=results
data.hist(alpha=0.5,column='diff',bins=10000)
data['diff'].plot(kind='hist')