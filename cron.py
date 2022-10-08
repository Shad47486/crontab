#import needed modules
import os 
import sys
import time 
import pandas as pd
import numpy as np
# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# where we input the data we are looking to get 
data = ('https://health.data.ny.gov/resource/xdss-u53e.csv')
# data will have an api that we are looking to grab 


# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/home/Reshad/crontab/testfile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
# the place i set the folder was differnt from where someone else may put their folder location
# was having trouble setting it as a dataframe and was told the pandas doesnt have to_csv or for df