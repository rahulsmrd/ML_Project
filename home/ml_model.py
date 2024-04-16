import numpy as np
import pandas as pd
from sklearn import tree
from home.utils import save_model

#<------------------------------------- Reading the training.csv file ------------------------------------->

df=pd.read_csv("home/training.csv")
DF= pd.read_csv('home/training.csv', index_col='prognosis')

#<------Replace the values in the imported file by pandas by the inbuilt function replace in pandas.-------->

disease_list=list(df['prognosis'].unique())
symptoms_list=list(df)
symptoms_list.pop()
count=0
for i in df.prognosis.unique():
    df.prognosis.replace({i:count},inplace=True)
    count+=1

#<------------------------------Training data------------------------------------------>
X= df[symptoms_list]
y = df[["prognosis"]]

    #<------------------------------ Decission Tree Training ------------------------------>
clf = tree.DecisionTreeClassifier() 
clf = clf.fit(X,y)
    
#<--------------------Saving Models to Desk using Joblib library----------------------->
save_model(clf)

def create_symptoms_data(symptoms):
    data=[]
    for i in range(132):
        if symptoms_list[i] in symptoms:
            data.append(1)
        else:
            data.append(0)
    return data

def get_disease(index):
    return disease_list[index]