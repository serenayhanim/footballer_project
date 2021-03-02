import os
import glob
import pandas as pd 

rio_files = glob.glob("*[0-9].csv")
df= pd.concat([pd.read_csv(file) for file in rio_files])
