import pandas as pd

# dff = pd.DataFrame({'col_a':['a','b','c'], 'col_b':[1,2,3]})
# print(dff)

# dff_ = pd.DataFrame(columns = dff.columns)
# n = []
# for i,row in dff.iterrows():
#     row['col_b']+=1
#     print('row')
#     print(row)
#     n.append(row)
#     print('N', n)


# dff_=pd.DataFrame(n)
# print(dff_)
df = pd.read_csv('newdf.csv')
df_ = df.drop_duplicates()
# print(df_.columns)
df_ = df_.drop(df_.columns[0], axis=1)
print(df_.columns)
df_.to_csv('datarade_df.csv',index = False)