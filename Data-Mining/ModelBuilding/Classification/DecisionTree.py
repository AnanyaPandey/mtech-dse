
# Building a decision tree from scratch.

import numpy as np
import pandas as pd
from pprint import pprint as pprint

try:
    # data_address = ''
    data = pd.read_csv("zoo.csv")
except:
    print("Data not found")

#Dopping the name # axis = 1 is column
data = data.drop('animal_name',axis=1)

def entropy(targetcol):
    element,count = np.unique(targetcol,return_counts=True)
    entropy = np.sum([-count[i]/np.sum(count)*np.log2(count[i]/np.sum(count)) for i in range(len(element))])
    return entropy

def infogain(data,split_attr,targetname = 'class_type'):
    total_entropy = entropy(data[targetname]) # entropy of the target variable
    value,count = np.unique(data[split_attr],return_counts=True)

    # calculating weighted entropy 
    weightd_entropy = np.sum([(count[i]/np.sum(count))*entropy(data.where(data[split_attr] ==value[i]).dropna()[targetname]) for i in range(len(value)) ])
    infomgain = total_entropy - weightd_entropy
    return infomgain

# Iterative dichotomizer
# original 
def ID3(data,originaldata,features,target='class_type',parentnodeclass=None):
    # if all target values have same value then it should return this value :
    if len(np.unique(data[target])) <= 1 :
        return np.unique(data[target])[0]
    
    # if data is empty
    elif len(data) ==0 :
        return np.unique(data[target])[np.argmax(np.unique(originaldata[target],return_counts=True)[1])]
    
    # if feature space is empty
    elif len(features) == 0:
        return parentnodeclass 
    
    # otherwise -> grow the tree
    else :
        parentnodeclass = np.unique(data[target])[np.argmax(np.unique(originaldata[target],return_counts=True)[1])]

    # selecting the splitting criteria (splitting attribute)
    itemvalues = [infogain(data,features,target) for each in features] # return the infogain for the passed feature for the data
    bestfeatureindex = np.argmax(itemvalues)
    bestfeature = features[bestfeatureindex]

    ## Create Tree Structure : 
    tree = {bestfeature:{}}

    ## remove the feastuer weith feature with best info gain because we included in node
    features = [i for i in features if i!= bestfeature]

    # Grow the tree branch 
    for value in np.unique(data[bestfeature]):
        value = value
        subdata = data.where(data[bestfeature]==value).dropna()
        # Creating a subtree - repeat for each node
        subtree = ID3(subdata,data,features,target,parentnodeclass)
        # Addd the sub tree
        tree[bestfeature][value] =subtree
    
    return tree

def predict(query, tree, default=1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]]
            except:
                return default
            result = tree[key][query[key]]
            if isinstance(result,dict):
                return predict(query,result)
            else:
                return result

def train_test_split(data):
    traindata = data.iloc[:80].reset_index(drop=True)
    testingdata = data.iloc[80:].reset_index(drop=True)
    return traindata,testingdata

traindata = train_test_split(data)[0]
testdata = train_test_split(data)[1]

def testaccuracy(data,tree):
    queries = data.iloc[:,:-1].to_dict(orient="records")
    predicted = pd.DataFrame(columns=["predicted"])
    for i in range(len(data)):
        predicted.loc[i,"predicted"] = predict(queries[i],tree,1.0)

    print("Prediction accuracy :",(np.sum(predicted["predicted"]==data["class_type"])/len(data)*100),'%')

# Training the tree and predicting the accuracy.
tree = ID3(traindata,traindata,traindata.columns[:-1])
pprint(tree)
testaccuracy(testdata,tree)

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
animal = pd.read_csv("zoo.csv")
X = animal.iloc[:,1:17]
y = animal.iloc[:,17]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
dclf = DecisionTreeClassifier(criterion="entropy")
dclf.fit(X_train,y_train)
ypred = dclf.predict(X_test)
from sklearn.metrics import accuracy_score
score = accuracy_score(ypred,y_test)
print("Using Sklearn Accuracy:",score*100,'%')

from sklearn import tree
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(dclf,
               feature_names = X.columns, 
               class_names=['1','2','3','4','5','6','7'],
               filled = True)
fig.savefig('imagename.png')
