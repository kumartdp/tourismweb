import pandas as pd
df=pd.read_csv('d.csv')
state=input("enter state")
district=input("enter district")
df1=df[(df['state']==state) & (df['district']==district)]
l=df1['success_rate'].nlargest(3).index.tolist()
x=[df.iloc[i]['crop'] for i in l]
print(x)

