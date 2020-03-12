# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14uWw7bnsXl8BsdQWCuYRSEbQ_-_5geUm
"""

class MyLinearRegression:
  def __init__(self,weight=0.0,bias=0.0,epochs=100,lr=0.001):
    self.weight=weight
    self.bias=bias
    self.epochs=epochs
    self.lr=lr
    self.cost=0
    self.ct=[]
  def update(self,x,y):
    wd=0;
    bd=0;
    for i in range(len(x)):
      bd+=-2*(y[i]-self.bias-self.weight*x[i])
      wd+=-2*x[i]*(y[i]-self.bias-self.weight*x[i])
    self.weight-=wd/len(x)*self.lr
    self.bias-=bd/len(x)*self.lr
  def cf(self,x,y):
    cost=0
    for i in range(len(x)):
      cost+=(self.bias + self.weight*x[i] - y[i])**2
    return cost/len(x)
  def predict(self,x):
    yp=[]
    for i in range(len(x)):
      yp.append(self.bias+self.weight*x[i])
    return yp
  def train(self,x,y):
    for i in range(self.epochs):
      self.update(x,y)
      self.cost=self.cf(x,y)
      self.ct.append(self.cost)
      print("Iteration:{}\t Weight:{}\t Bias:{}\t Cost:{}\t".format(i,self.weight,self.bias,self.cost))

X=[2.5,5.1,3.2,8.5,3.5,1.5,9.2,5.5,8.3,2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,4.8,3.8,6.9,7.8]
Y=[21,47,27,75,30,20,88,60,81,25,85,62,41,42,17,95,30,24,67,69,30,54,35,76,86]

import matplotlib.pyplot as plt
plt.scatter(X,Y,color="blue")
plt.show()

reg=MyLinearRegression()
reg.train(X,Y)

plt.plot(reg.ct,color="blue")

plt.plot(X,reg.predict(X),color="blue")
plt.scatter(X,Y,color="green")