import numpy
import pandas
import matplotlib.pyplot as plt

dataset = pd.read_csv("mall.csv")
X = dataset[:,3:5].values

# using elbow method

from sklearn.cluster import KMeans
wcss=[] # this is a python list 
for i in range(1,11):
	km = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=111) # random initialization can put us in trap # ninit is no of times k means is run with diff centroids
	km.fit(X)
	wcss.append(km.inertia_)	# WCSS within cluster sum of squares also called : Inertia
	
plt.plot(range(1,11),wcss)
plt.title("K means cluster with elbow method")

# chose appropriate K 
km=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=111)
y_kmeans = km.fit_predict(X)

plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1], s = 100, c = 'red', label='cluster 1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1], s = 100, c = 'blue', label='cluster 2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1], s = 100, c = 'green', label='cluster 3')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1], s = 100, c = 'magenta', label='cluster 4')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1], s = 100, c = 'grey', label='cluster 5')
plt.scatter(km.cluster_centers_[:,0], km.cluster_[:,1], s=300,c='yellow', label='Centroids')

plt.title("Cluster of clients")
plt.xlabel("income K$")
plt.ylabel("Speding score")
plt.legend()
plt.show()

