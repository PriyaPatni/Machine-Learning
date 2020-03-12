# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bSeaHGmcO07TFQYmjr9ctqAJTeKUyd8F

###LINEAR REGRESSION

1. Import Modules
"""

import numpy as np
import matplotlib.pyplot as plt

"""2. Data providing and plot"""

X = np.array([5, 15, 25, 35, 45, 55]).reshape((-1,1))
Y = np.array([5, 20, 14, 32, 22, 38])
plt.scatter(X, Y, color="red")
plt.show()

"""3. Creating a model and fitting it"""

from sklearn.linear_model import LinearRegression
#model = LinearRegression() # crearte the object of the LinearRegression
#model.fit(X, Y) # call method fit on X,Y
# this two statements can be written as one


model = LinearRegression().fit(X,Y)

"""4. Get results"""

r_sq = model.score(X, Y)
print("Coeffecient of determination: ", r_sq)
print("Intercept: ",model.intercept_)
print("Slope: ",model.coef_)

"""5. Predict the responses"""

y_pre
d = model.predict(X)
print("Predicted responses: ", y_pred)

plt.scatter(X,Y, color="blue")
plt.scatter(X, y_pred, color="green")
plt.show()