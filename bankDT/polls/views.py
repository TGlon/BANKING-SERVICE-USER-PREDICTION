from django.shortcuts import render, HttpResponse
from .forms import BankClientForm
from .models import Label
def index(request):
    if request.method == 'POST':
        b = BankClientForm(request.POST)
        if b.is_valid():
            B = b.cleaned_data
            label = Predict(B)
            l = Label(label=label[0])
            print(l.label)
            return render(request, 'polls/index.html', {'f':B, 'l':l})
    else:
        client = BankClientForm()
        l = Label()
        return render(request, 'polls/index.html', {'f':client, 'l':l})

# Create your views here.


from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import random 
import pandas as pd
import numpy as np

def Predict(X_test):
    train = pd.read_csv('D:/project_khaikhoang/bank-additional/bank-additional/bank-additional-full.csv', delimiter = ';')
    X_test = pd.DataFrame(X_test, index=[0])
    print(X_test)
    #====================================================================
    train.drop(['duration','contact','month','day_of_week','default','pdays',],axis=1,inplace=True)
    #===================================================================
    # chuyển 'basic.6y','basic.4y', 'basic.9y' về basic
    train.replace(['basic.6y','basic.4y', 'basic.9y'], 'basic', inplace=True)
    # print(train)
    train = train.rename(columns={"emp.var.rate":'empvarrate',"cons.price.idx":"conspriceidx", "cons.conf.idx":"consconfidx", "nr.employed":"nremployed"})
    print(train.head(1))
    #====================================================================
    y ={'yes' : 1, 'no' : 0}
    train['y'] = train['y'].map(lambda x: y[x])
    # print(train['y'].value_counts())
    y = train['y']
    train.drop(['y'], axis = 1, inplace = True) 
    # print(train.head)
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    le.fit(train['job'])
    train.job = le.transform(train.job)
    X_test.job = le.transform(X_test.job)
    le.fit(train['marital'])
    train.marital = le.transform(train.marital)
    X_test.marital = le.transform(X_test.marital)
    le.fit(train['education'])
    train.education = le.transform(train.education)
    X_test.education = le.transform(X_test.education)
    le.fit(train['housing'])
    train.housing = le.transform(train.housing)
    X_test.housing = le.transform(X_test.housing)
    le.fit(train['loan'])
    train.loan = le.transform(train.loan)
    X_test.loan = le.transform(X_test.loan)
    le.fit(train['poutcome'])
    train.poutcome = le.transform(train.poutcome)
    X_test.poutcome = le.transform(X_test.poutcome)
    # print(train.head)
    #=============================================================================
    tree = DecisionTreeClassifier(criterion='entropy')
    x_train, x_test, y_train, y_test = train_test_split(train, y, test_size=1/3.0, random_state=2524)
    tree.fit(x_train, y_train)
    y_pred = tree.predict(X_test)
    return y_pred






