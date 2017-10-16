from __future__ import division
import sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt





iterations=10000
batch_size=1


df=pd.read_csv('LR_dataset.csv')
y=df['type'].reshape(-1)



learning_rate=0.01
val_list=[]

for key,val in df.items():
	if key!='type':
		val_list.append(val)
X=np.vstack(val_list)
print(X.T)
X=X.T

n_X=X.shape[0]

bias=np.ones([n_X,1])
X=np.hstack([bias,X])



params=np.random.normal(0,1,[1,9])


def logistic(z):
	return 1/(1+np.exp(-z))

# Stochastic gradient descent	




for iteration in range(iterations):
	feed_X=X[(iteration)%n_X:(iteration+batch_size)%n_X]
	feed_Y=y[(iteration)%n_X:(iteration+batch_size)%n_X]

	params=params+learning_rate*np.dot((np.array([feed_Y])-logistic(np.dot(params,feed_X.T))),feed_X)
print(params)

params=np.random.normal(0,1,[1,9])

for iteration in range(iterations):
	

	params=params+learning_rate*np.dot((np.array([y])-logistic(np.dot(params,X.T))),X)

print(params)





