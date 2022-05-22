
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')
X = data.iloc[:,[2,3]].values
y = data.iloc[:,4].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix, f1_score
cm = confusion_matrix(y_pred,y_test)
f1_sc = f1_score(y_pred,y_test)
print("Confusion Matrix : ",cm)
print("F1 Score : ",f1_sc)

def plot_decision_boundry(X,y):
	from matplotlib.colors import ListedColormap
	X_set, y_set = X, y
	X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
	                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
	plt.contourf(X1, X2, clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
	             alpha = 0.75, cmap=ListedColormap(('white', 'yellow')))
	plt.xlim(X1.min(), X1.max())
	plt.ylim(X2.min(), X2.max())
	for i, j in enumerate(np.unique(y_set)):
	    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
	                c = ListedColormap(('red', 'green'))(i), label = j)
	plt.title('Classifier (Training set)')
	plt.xlabel('Age')
	plt.ylabel('Estimated Salary')
	plt.legend()
	plt.show()

plot_decision_boundry(X_train,y_train)