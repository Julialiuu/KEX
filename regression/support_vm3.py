print(__doc__)

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


csv_file='all.csv'


df=pd.read_csv(csv_file)
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)
df.loc[:,:] = scaled_values

y=df['revenue']
X=df['production_budget']

y=y.reshape((len(X),1))
y=y.ravel()
X=X.reshape((len(X),1))

print(X)
print(y)


print(1)
svr_lin = SVR(kernel='linear', C=1e3)
print(2)
y_lin = svr_lin.fit(X, y).predict(X)
print(3)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
