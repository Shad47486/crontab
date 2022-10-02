#import needed modules
import os 
import sys
import time 

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# where we input the data we are looking to get 
data = ('https://health.data.ny.gov/resource/xdss-u53e.json')
# data will have an api that we are looking to grab once a day  

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
