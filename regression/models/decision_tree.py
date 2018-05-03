

print(__doc__)

# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score

#import dataset
csv_file='actor.csv'

df=pd.read_csv(csv_file)

x = np.array(df['actor'])
X=x.reshape(len(x),1)
x=x.transpose()
y=df['revenue']
y=y.reshape((len(X),1))
y=y.ravel()

X, x_test, y, y_test = train_test_split(X, y, test_size = 0.2)


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=3, min_samples_leaf=5)
regr_2 = RandomForestRegressor(max_depth=3)
regr_1.fit(X, y)
regr_2.fit(X, y)
y_1 =regr_1.predict(x_test)
y_2 =regr_2.predict(x_test)
print('r2_y1:',r2_score(y_test,y_1))
print('r2_y2:',r2_score(y_test,y_2))

# Predict
X_grid = np.arange(min(x_test), max(x_test), 0.1)
print(X_grid)
X_grid = X_grid.reshape((len(X_grid), 1))
y_1 = regr_1.predict(X_grid)
y_2 = regr_2.predict(X_grid)
#print(y_1)
# Plot the results
plt.figure()
plt.scatter(x_test, y_test, s=20, edgecolor="black",
            c="darkorange", label="data")
plt.plot(X_grid, y_1, color="cornflowerblue",
         label="max_depth=2", linewidth=2)
plt.plot(X_grid, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
#plt.plot(X_grid, y_2, color = 'blue')
#plt.plot(X_grid, y_2, color = 'blue')
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
