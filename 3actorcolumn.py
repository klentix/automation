import pandas as pd
import os
import csv
# read the csv file

df = pd.read_csv('movie.csv',delimiter=',')

spec_chars = ["[","]"," '","'"]
for char in spec_chars:
    df['cast'] = df['cast'].str.replace(char,'')
#
# #split the string of actor names into list
df['cast'] = df['cast'].str.split(',')

#
# #explode the list of actors into separate rows
df = df.explode('cast').reset_index(drop =True)
#
# #display df
print (df)
#
# #move result into new csv file
df.to_csv('cast.csv',index=False)
# os.remove('movie.csv')
#

