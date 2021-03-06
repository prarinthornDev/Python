# -*- coding: utf-8 -*-
"""056 DecisionTree .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZnKTmtNP4jtpB4wvsxpVpYxfGv_dgXsr

# **Data + Convert**
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/udacity/machine-learning/master/projects/student_intervention/student-data.csv')
df.head()

df.passed.value_counts()

df.columns

sns.pairplot(df , vars=['famsize','Pstatus','Medu','Fedu','Mjob','Fjob','guardian','studytime','failures','activities','nursery','higher','internet','famrel','freetime','goout','absences']);

from sklearn.model_selection import  train_test_split  
from sklearn.metrics import  roc_curve, roc_auc_score  
import math

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

df.columns

x_train = df[['famsize','Pstatus','Medu','Fedu','Mjob','Fjob','guardian','studytime','failures','activities','nursery','higher','internet','famrel','freetime','goout','absences']]
y_train = df.passed


x_train , x_test , y_train , y_test = train_test_split(
    df[['famsize','Pstatus','Medu','Fedu','Mjob','Fjob','guardian','studytime','failures','activities','nursery','higher','internet','famrel','freetime','goout','absences']],
    df.passed,
    test_size=.1
)

x_train.head()

y_train.head()

x_test.head()

y_test.head()

model = DecisionTreeClassifier()
model

x_train = x_train.replace('LE3', 0)
x_train = x_train.replace('GT3', 1)
x_train = x_train.replace('T', 1)
x_train = x_train.replace('A', 0)
x_train = x_train.replace('other', 0)
x_train = x_train.replace('services', 1)
x_train = x_train.replace('teacher', 2)
x_train = x_train.replace('at_home', 3)
x_train = x_train.replace('health', 4)

x_train = x_train.replace('mother', 1)
x_train = x_train.replace('father', 2)

x_train = x_train.replace('yes', 1)
x_train = x_train.replace('no', 0)

x_train.head()

model.fit(x_train,y_train)

model.score(x_train,y_train)

x_test = x_test.replace('LE3', 0)
x_test = x_test.replace('GT3', 1)
x_test = x_test.replace('T', 1)
x_test = x_test.replace('A', 0)
x_test = x_test.replace('other', 0)
x_test = x_test.replace('services', 1)
x_test = x_test.replace('teacher', 2)
x_test = x_test.replace('at_home', 3)
x_test = x_test.replace('health', 4)

x_test = x_test.replace('mother', 1)
x_test = x_test.replace('father', 2)

x_test = x_test.replace('yes', 1)
x_test = x_test.replace('no', 0)

x_test.head()

predicted = model.predict(x_test)

model.predict(x_test)

x_test.columns

x_test['famsize']

x_test = x_test.replace('LE3', 0)
x_test = x_test.replace('GT3', 1)
x_test = x_test.replace('T', 1)
x_test = x_test.replace('A', 0)
x_test = x_test.replace('other', 0)
x_test = x_test.replace('services', 1)
x_test = x_test.replace('teacher', 2)
x_test = x_test.replace('at_home', 3)
x_test = x_test.replace('health', 4)

x_test = x_test.replace('mother', 1)
x_test = x_test.replace('father', 2)

x_test = x_test.replace('yes', 1)
x_test = x_test.replace('no', 0)

data = {'famsize':[0],
        'Pstatus':[0],
        'Medu':[0],
        'Fedu':[0],
        'Mjob':[0],
        'Fjob':[0],
        'guardian':[0],
        'studytime':[0],
        'failures':[0],
        'activities':[0],
        'nursery':[0],
        'higher':[0],
        'internet':[1],
        'famrel':[0],
        'freetime':[0],
        'goout':[0],
        'absences':[0],
        }

dataTest = pd.DataFrame(data)

dataTest

model.predict(dataTest)

model.predict(x_test)

print(y_test)

"""# ***REPORT***"""

from sklearn.metrics import  confusion_matrix,classification_report,accuracy_score

dx=pd.DataFrame({'y_true': y_test, 'y_predice': predicted})

dx[dx.y_true != dx.y_predice].count()

print(accuracy_score(y_test,predicted))