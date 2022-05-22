
# KNN (K Nearest Neighbours)

#import Library
#import data
#train test split
#feature scaling X

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighboursClassifier(n_neighbors=5,metric='minkowski',p=2)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

# confusion matrix for binary classification 
from sklaern.metrics import confusion_matrix





