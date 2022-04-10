import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path 
import sys 


# check the dataset is inside files 

datapath = 'data/'
if os.path.isdir(datapath): 
    required_files = ["Pre_Req.csv"]
    for file in required_files:
        filedir = os.path.isfile(datapath+file)
        if not filedir:
            print(file + " is not in Folder")
            sys.exit()
        else:
            continue