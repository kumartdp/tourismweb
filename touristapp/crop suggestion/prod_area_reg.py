import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
datset=pa.read_csv("crop_final_details_apy.csv")
datset_district=datset.drop_duplicates('District_Name')['District_Name']
regressor=LinearRegression()
ppp=[]
for i in datset_district:
    value_district=datset.loc[(datset['District_Name'] == i)].drop_duplicates('Crop')
    for j in value_district['Crop']:
        www=datset.loc[(datset['Crop'] == j) & (datset['District_Name'] == i)]
        try:
            x= www.iloc[:,5:6].values
            y= www.iloc[:,7:8].values
            xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
            regressor.fit(xtrain,ytrain)
            predy=regressor.predict(xtest)
            pred_min=predy.mean()-0.2
            pred_max=predy.mean()+0.2
            pred_mean=(pred_max+pred_min)/2
            state=list(www.loc[(www['District_Name'] == i)].drop_duplicates('State_Name')['State_Name'])
            l=[state[0],i,j,www['prod_area'].mean(),pred_mean]
            ppp.append(l)
            print(l)
        except ValueError:
            print(www)
p=pa.DataFrame(data=ppp)
p.to_csv('prod_area.csv')
        
    
