
data = read.csv('data.csv')
data=data[,3:5]
library(caTools)
set.seed(123)
split=sample.split(data$purchased, SplitRatio =0.8)
train = subset(data,split=TRUE)
test = subset(data,split=FALSE)


trainset = scale(train[,2:3])
testset = scale(test[,1:2])

clf = glm(formula=purchased ~ ., family=binomial,data=trainset) 
# dot is all variables 

prob_pred = predict(clf,type='response',newdata=testset[-3])
y_pred = ifelse(prob_pred > 0.5, 1,0)
cm = table(testset[,3],y_pred)
