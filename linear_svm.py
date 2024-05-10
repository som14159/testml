import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn import svm

X,y = make_moons(n_samples=100,noise=0.1)
svc = svm.SVC(kernel='linear').fit(X,y)
xx,yy = np.meshgrid(np.arange(X[:,0].min(),X[:,0].max(),0.01),np.arange(X[:,1].min(),X[:,1].max(),0.01))
result = []
for i in range(len(xx)):
    for j in range(len(xx[i])):
        result.append([xx[i][j],yy[i][j]])

Z = svc.predict(result)
Z = Z.reshape(xx.shape)

plt.contour(xx,yy,Z)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()

