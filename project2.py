#import library and model

import pandas as pd
import numpy  as np
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

#reading  data from csv file

df=pd.read_csv("PerpData.csv")

#classification of data

x=df[['PERCENTAGE', 'BACKLOG', 'INTERNSHIP', 'FIRSTROUND','COMMUNICATIONSKILLLS']]
y=df['Hired']

#Function that will compute and take Decision

def DecisionTreeClassifier12(per1,backlog1,intern1,round1,comm1):
    dtree = DecisionTreeClassifier()
    dtree.fit(x,y)
    return dtree.predict([[per1,backlog1,intern1,round1,comm1]])

def randomforest12(per1,backlog1,intern1,round1,comm1):
    rfc = RandomForestClassifier(n_estimators=10)
    rfc.fit(x,y)
    return rfc.predict([[per1,backlog1,intern1,round1,comm1]])[0]


def regression12(per1,backlog1,intern1,round1,comm1):
    logmodel = LogisticRegression()
    logmodel.fit(x,y)
    return logmodel.predict([[per1,backlog1,intern1,round1,comm1]])
