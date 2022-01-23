import pandas as pd

dff = pd.DataFrame({'col_a':['a','b','c'], 'col_b':[1,2,3]})
print(dff)

dff_ = pd.DataFrame(columns = dff.columns)
n = []
for i,row in dff.iterrows():
    row['col_b']+=1
    print('row')
    print(row)
    n.append(row)
    print('N', n)


dff_=pd.DataFrame(n)
print(dff_)