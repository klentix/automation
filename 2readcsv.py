#import csv

import pandas as pd


# namelist = []

df = pd.read_csv('movie.csv')
keep_col = ['cast']
newdf = df[keep_col]
newdf.to_csv('movie.csv',index =False)




