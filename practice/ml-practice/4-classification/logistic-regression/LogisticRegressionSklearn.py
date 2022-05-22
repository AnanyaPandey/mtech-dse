# Logistic Regression #

import numpy as np
import pandas as pd

import sklearn.model_selection as train_test_split
 X_train,X_test,y_train,y_test = train_test_split(test_size=0.3,random_state=0)

 from sklearn.preprocessing import StandardScaler
 SS=StandardScaler()
 X_train = SS.fit_transform(X_train)
 X_test = SS.fit_transform(X_test)

 from sklearn.linear_model import LogisticRegression
 clf = LogisticRegression(random_state=0)
 clf.fit(X_train,y_train)

 y_pred = clf.predict(X_test)
 from sklearn.metrics import confusion_matrix
 cm=confusion_matrix(y_test,y_pred)
 print(cm)

 '''
TP FP
TP FN

CorrectPrediction WrongPreduction
WrongPreduction  CorrectPrediction

 Check Accuracy - by using accuracy  score  sensetivity, specificity and Precision 

Sensitivity (Recall) = No. of True Positives / (No. of True Positives + No. of False Negatives)
Sensitivity = TP / (TP + FN)

Specificity = No. of True Negatives / (No. of True Negatives + No. of False Positives)
Specificity = TN / (TN + FP)

Precision = No. of True Positives / (No. of True Positives + No. of False Positives)
Precision = TP / (TP + FP)

For two categories F1 score is also the metric

F1 = 2 * (precision * recall) / (precision + recall)

'''

def plot_decision_boundry(X,y):
	X_set,y_set = X,y
	import matplotlib.pyplot as plt
	from matplotlib.colors import ListedColormap
	X1,X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1, stop=X_set[:,0].max()+1, step=0.01),
		np.arange(start=X_set[:,1].min()-1, stop=X_set[:,1].max()+1, step=0.01)
		)
	plt.contour(X1,X2,clf.predict(np.rray([X1.ravel(),X2.ravel()]).T ).reshape(X1.shape),alpha=0.75)
	plt.xlim(X1.min(),X1.max())
	plt.ylim(X2.min(),X2.max())
	for i,j in enumerate(np.unique(y_set)):
		plt.scatter(X_set[y_set==j,0], X_set[y_set==j,1], c=ListedColormap(('red','green'))(i),label=j)

	plt.title('Logistic Regression Classification Boundry')
	plt.xlabel('X Label')
	plt.ylabel('Y Label')
	plt.legend()
	plt.show()
	




