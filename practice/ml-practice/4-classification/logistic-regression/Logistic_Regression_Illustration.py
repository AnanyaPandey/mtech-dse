#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import pandas as pd
from  sklearn.model_selection import  train_test_split
from sklearn.preprocessing import StandardScaler


# In[72]:


get_ipython().system('ls')


# In[73]:


data=pd.read_csv('Social_Network_Ads.csv')
data.head()


# In[74]:


X = data[['Age','EstimatedSalary']]
y=data['Purchased']


# In[75]:


#X['Sex_binary']=X['Gender'].map({'Male':1,'Female':0})
#X=X.drop(['Gender'],axis=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)


# In[76]:


from sklearn.preprocessing import StandardScaler
SS=StandardScaler()
X_train = SS.fit_transform(X_train)
X_test = SS.fit_transform(X_test)


# In[77]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0)
clf.fit(X_train,y_train)


# In[78]:


y_pred = clf.predict(X_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)


# In[82]:


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


# In[86]:


def plot_decision_boundry(X,y):
	X_set,y_set = X,y
	import matplotlib.pyplot as plt
	from matplotlib.colors import ListedColormap
	X1,X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1, stop=X_set[:,0].max()+1, step=0.01),
						np.arange(start=X_set[:,1].min()-1, stop=X_set[:,1].max()+1, step=0.01)
		)
	plt.contour(X1,X2,clf.predict(np.array([X1.ravel(),X2.ravel()]).T ).reshape(X1.shape),alpha=0.75)
	plt.xlim(X1.min(),X1.max())
	plt.ylim(X2.min(),X2.max())
	for i,j in enumerate(np.unique(y_set)):
		plt.scatter(X_set[y_set==j,0], X_set[y_set==j,1], c=ListedColormap(('red','green'))(i),label=j)

	plt.title('Logistic Regression Classification Boundry')
	plt.xlabel('X Label')
	plt.ylabel('Y Label')
	plt.legend()
	plt.show()
	


# In[87]:


plot_decision_boundry(X_train,y_train)


# In[ ]:




