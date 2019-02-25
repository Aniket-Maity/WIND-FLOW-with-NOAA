"""
Created on Sat Feb 23 12:33:09 2019

@author: Aniket Maity
"""

import numpy as np
import datetime as dt
from skimage.io import imread
import matplotlib.pyplot as plt

def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + dt.timedelta(n)
        
folder = "E:\\python_2019\\images\\"
startDate = dt.date(2017,1,1)
endDate = dt.date(2017,5,31)

for date in daterange(startDate,endDate):
      print(date.strftime("%Y-%m-%d"))
    
    for v in range(0,22,3):
        #print("0"+str(v) if v < 10 else str(v))
        v = "-0"+str(v) if v < 10 else "-"+str(v)
        try:
            img_sk = imread("https://www.ncdc.noaa.gov/gibbs/image/GRD-1/IR/"+date.strftime("%Y-%m-%d")+v)
            
            crop_img = img_sk[200:500, 1100:1500]
            plt.imsave(folder+date.strftime("%Y-%m-%d")+v+'.jpg',crop_img)
            print(date.strftime("%Y-%m-%d")+v)
        except:
            pass
