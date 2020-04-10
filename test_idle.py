import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
a=['A','B','C']
b=[15,16,2]
c=[1,0,1]
my_frame=pd.DataFrame({'name':a,'year':b,'result':c},
    columns=['name','year','result'],index=['a','b','c'])
my_frame.index.name="row"
my_frame.columns.name='information'

print(my_frame.columns)
print(my_frame.index)
print(my_frame)

print('#########################################################')
#print(my_frame.reindex(range(6),method='ffill'))
print('##########################################################')
#print(my_frame.reindex(range(6),method='bfill'))
print('##########################################################')
#print(my_frame.reindex(columns=['name','sex','result']))

print('########################################################')
my_ser=pd.Series(range(4),index=['a','b','f','e'])
df_1=pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','e','d'],index=[0,2,1])
df_2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=['a','b','c','d','e'])
df_1.iloc[0,0]=-100
print(df_1)
print('########################################################')
print(df_1.sort_index(axis=1).sort_index())
print('##########################################################')
s=pd.Series([7,-7,-5,4,4,4,6])
print(s.rank(method='dense  '))
    