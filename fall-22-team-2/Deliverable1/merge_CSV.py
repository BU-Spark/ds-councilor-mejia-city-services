import pandas as pd
from functools import reduce




#df1 = pd.read_csv('Cannabis.csv', on_bad_lines='skip')
df1 = pd.read_csv('neighborhoods.csv') # good
df2 = pd.read_csv('Capital_budget_final.csv') #good
df3 = pd.read_csv('food.csv') #good
df4 = pd.read_csv('liquor.csv') #good 
df5 = pd.read_csv('cannabis.csv')

data_frames = [df1, df2, df3, df4, df5]

df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Neighborhood'],
                                            how='outer'), data_frames).fillna('void')

#temp.set_index('Neighborhood', inplace = True)
#temp.to_csv('merged.csv')





