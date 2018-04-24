

print(__doc__)

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold
import csv
from math import sqrt
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# #############################################################################
# Generate sample data
df=pd.read_csv("wiki_eng_sf_rating.csv")

y=df['revenue']
#y=y.reshape(len(y),1)

x = df['imdb_rating']
X=x.reshape(len(x),1)



"""
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
"""
# #############################################################################
# Add noise to targets
#y[::5] += 3 * (0.5 - np.random.rand(8))

# #############################################################################
# Fit regression model
print('hej')
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
print(1)
svr_lin = SVR(kernel='linear', C=1e3)
print(2)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
print(3)
y_rbf = svr_rbf.fit(X, y).predict(X)
print(4)
y_lin = svr_lin.fit(X, y).predict(X)
print(5)
y_poly = svr_poly.fit(X, y).predict(X)
print('hola')

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
