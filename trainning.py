import pandas as pd
import numpy as np

train = pd.read_csv('./bank-additional/bank-additional/bank-additional-full.csv', delimiter = ';')
#====================================================================
train.drop(['duration','contact','month','day_of_week','default','pdays',],axis=1,inplace=True)
#===================================================================
#chuyển 'basic.6y','basic.4y', 'basic.9y' về basic
# train.replace(['basic.6y','basic.4y', 'basic.9y'], 'basic', inplace=True)
# # print(train)
# #======================================================================
# #====================================================================
# # chuyển đổi những dữ liệu kiểu string về float
# y ={'yes' : 1, 'no' : 0}
# train['y'] = train['y'].map(lambda x: y[x])
# # print(train['y'].value_counts())
# y = train['y']
# train.drop(['y'], axis = 1, inplace = True) 
# # print(train.head)
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# le.fit(train['job'])
# train.job = le.transform(train.job)
# le.fit(train['marital'])
# train.marital = le.transform(train.marital)
# le.fit(train['education'])
# train.education = le.transform(train.education)
# le.fit(train['housing'])
# train.housing = le.transform(train.housing)
# le.fit(train['loan'])
# train.loan = le.transform(train.loan)
# le.fit(train['poutcome'])
# train.poutcome = le.transform(train.poutcome)
# # print(train.head)

# #=======================================================================
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import KFold
# from sklearn.metrics import accuracy_score
# import random 

# tree = DecisionTreeClassifier(criterion='entropy')
# x_train, x_test, y_train, y_test = train_test_split(train, y, test_size=1/3.0, random_state=2524)
# tree.fit(x_train, y_train)
# y_pred = tree.predict(x_test)

print(train.iloc[1,:])





