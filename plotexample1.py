# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:52:57 2016

@author: jmf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = 20
time = np.arange(0,10).reshape(10,1)
d1data = np.append(np.append(time,np.random.rand(10).reshape(10,1)+base,axis=1),np.ones((10,1)),axis=1)
d2data = np.append(np.append(time,np.random.rand(10).reshape(10,1)+base+0.1,axis=1),np.ones((10,1))*2,axis=1)
d3data = np.append(np.append(time,np.random.rand(10).reshape(10,1)+base+0.2,axis=1),np.ones((10,1))*3,axis=1)

data = np.append(np.append(d1data,d2data,axis=0),d3data,axis=0)

df = pd.DataFrame(data,columns=["time","vals","districtNum"])

fig = plt.figure(0)
colors = ['r','b','g']
for i in range(0,3):
    subset = df[df["districtNum"]==i+1]
    plt.plot(subset["time"].tolist(),subset["vals"].tolist(),color=colors[i])

plt.axis([0,10,base-base/5,base+1+base/5])
plt.show()

