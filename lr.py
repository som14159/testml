import numpy as np
import matplotlib.pyplot as plt
def findSlope(x,y):
    n=len(x)
    XY=0
    X2=0
    Y=0
    X=0
    for i in range(n):
        XY += x[i] * y[i]
        X2 += x[i] * x[i]
        X += x[i]
        Y += y[i]
    return (n*XY-X*Y)/(n*X2-X*X)

def findIntercept(x,y,m):

    n=len(x)

    X=0

    Y=0

    for i in range(n):

        X += x[i]

        Y += y[i]

    return (Y-m*X)/n

def plotRegressionLine(m,c,x,y):

    X = np.arange(0,10,0.02)

    plt.plot(x, y, '.')

    plt.plot(X, X * m + c, '--')

    plt.show()

def predict(x,m,c):

    return m*x+c

n=int(input("Enter no of datapoints"))

x=[]

y=[]

for i in range(n):

    x.append(int(input("X:")))

    y.append(int(input("Y:")))

m = findSlope(x,y)

c = findIntercept(x,y,m)

plotRegressionLine(m,c,x,y)

x_test=int(input("Enter a value to test"))

print("The prediction is:",predict(x_test , m, c))