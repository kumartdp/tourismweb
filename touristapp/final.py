import pandas as pd
def get(st,dist):

    df=pd.read_csv('d.csv')
    state=st
    district=dist
    df1=df[(df['state']==state) & (df['district']==district)]
    l=df1['success_rate'].nlargest(3).index.tolist()
    x=[df.iloc[i]['crop'] for i in l]
    return x


