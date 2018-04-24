#import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold
import csv
from math import sqrt
import pandas as pd
from sklearn import svm
import numpy as np
import warnings
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
warnings.simplefilter(action='ignore', category=FutureWarning)

#from matplotlib import pyplot
#from mpl_toolkits.mplot3d import Axes3D
number_of_splits = 5

csv_file='imdb_rating.csv'


df=pd.read_csv(csv_file)
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)
df.loc[:,:] = scaled_values

y=df['revenue']
X=df['imdb_rating']

y=y.reshape((len(X),1))
y=y.ravel()
X=X.reshape((len(X),1))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

"""
#x = np.array([df['production_budget'], df['imdb_rating']])
x = np.array([df['wiki_en'], df['sf_rating']])
#x = np.array([df['production_budget'], df['imdb_rating'],df['wiki_en'],df['wiki_sv'],df['sf_rating']])
x = x.transpose()
"""



clf = svm.SVR(kernel='poly',degree=300, C=1e3)
error =  []
coeficient = 0
MAE = 0
MSE = 0
Root_MSE = 0
r2 = 0



prediction=clf.fit(x_train,y_train).predict(x_test)


#coeficient += clf.coef_
MAE = mean_absolute_error(y_test, prediction)
MSE = mean_squared_error(y_test, prediction)
Root_MSE = np.sqrt(mean_squared_error(y_test, prediction))
r2 = r2_score(y_test, prediction)

print('Coefficients: \n', coeficient)
print('Mean Absolute Error:', MAE)
print('Mean Squared Error:', MSE)
print('Root Mean Squared Error:', Root_MSE)
print("r2_score:", r2)
"""
plt.scatter(x_test,y_test, color='black')
plt.plot(x_test,prediction,color='red',linewidth=3)

plt.title('Test Data')
plt.ylabel('revenue')
plt.xlabel('imdb_rating')

plt.xticks(())
plt.yticks(())

plt.show()
"""
lw = 2
plt.scatter(x_test, y_test, color='darkorange', label='data')
plt.hold('on')
plt.plot(x_test, prediction, color='c', lw=lw, label='Linear model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
