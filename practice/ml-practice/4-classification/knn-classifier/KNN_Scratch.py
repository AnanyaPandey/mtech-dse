import numpy as np
from sklearn import datasets
import random,operator
iris = datasets.load_iris()

iris_data = iris.data
iris_labels = iris.target

print(iris_data[79])
print(iris_labels[79])

np.random.seed(42)
indices = np.random.permutation(len(iris_data))

Numberofsample = 12
learndataset = iris_data[indices[:-Numberofsample]]
learndatasetLabels = iris_labels[indices[:-Numberofsample]]

Testdata = iris_data[indieces[-Numberofsample:]]
TestdataLabels = iris_labels[indices[-Numberofsample:]]

def distance(instance1,instance2):
	instance1 = np.array(instance1)
	instance2 = np.array(instance2)
	return np.linalg.norm(instance1-instance2)

def get_neighbour(TrainData,TrainLabels,TestInstance,k,distance=distance):
	distances=[]
	for i in rage(len(TrainData)):
		dist = distance(TestInstance,TrainData[i])
		distances.append(np.array(TrainData[i],dist,TrainLabels[i]))
		# OR distances.append((TrainData[i],dist,TrainLabels[i]))
		distances.sort(key=lambda x:x[1]) # sorting as per distance which is X[1] X[0] is trainingdata
		neighbors = distances[:k] # everything upto k 
	return neighbors

def getresponse(neighbors):
	classvotes = []
	for x in range(len(neighbors):
		response = neighbors[x][-1]
		if response in classvotes:
			classvotes[response] += 1
		else :
			classvotes[response] = 1
	sortedvotes = sorted(classvotes.iteritems(), key=operator.itemgetter(1),reverse=True)
	return sortedvotes[0][0]



