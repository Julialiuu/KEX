# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold
import csv
from math import sqrt
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
warnings.simplefilter(action='ignore', category=FutureWarning)

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true).ravel(), np.array(y_pred).ravel()
    value=0
    for number in range(len(y_true)):
        #print(abs(np.take(y_true,number)-np.take(y_pred,number))/(np.take(y_true,number)))
        value+=abs(np.take(y_true,number)-np.take(y_pred,number))/(np.take(y_true,number))
    answer=(value/len(y_true))*100

    # print("Y_TRUE: ", y_true)
    # print("Y_pred: ", y_pred)

    #return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return answer



def cross_vali(csv_file,y_header,x_header, number_of_splits,titel, y_label,x_label):
    #read data from file and normalize it
    df=pd.read_csv(csv_file)
    df = df[df[x_header] != 0]
    max_y=max(df['revenue'])
    print(max_y)
    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(df)
    df.loc[:,:] = scaled_values

    y=df[y_header]
    y=y.reshape(len(y),1)
    y=y.ravel()

    x = df[x_header]
    X=x.reshape(len(x),1)


    #split the trainingdata and testdata
    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    X, x_test, y, y_test = train_test_split(X, y, test_size = 0.2)

    # Fit regression model
    #regr_1 = DecisionTreeRegressor(max_depth=3, min_samples_leaf=5)
    regr_1 = linear_model.LinearRegression()
    regr_2 = RandomForestRegressor(max_depth=3)
    regr_3 = KNeighborsRegressor(3, weights='distance')
    regr_1.fit(X, y)
    regr_2.fit(X, y)
    regr_3.fit(X, y)
    y_1 =regr_1.predict(x_test)
    y_2 =regr_2.predict(x_test)
    y_3 =regr_3.predict(x_test)
    # print(y_test,y_1)
    print(x_label)
    print('r2_y1:',r2_score(y_test,y_1))
    print('r2_y2:',r2_score(y_test,y_2))
    print('r2_y3:',r2_score(y_test,y_3))
    print('MAPE_y1:',mean_absolute_percentage_error(y_test, y_1))
    print('MAPE_y2:',mean_absolute_percentage_error(y_test, y_2))
    print('MAPE_y3:',mean_absolute_percentage_error(y_test, y_3))
    #
    # print("y_test ", y_test)
    # print("Y_1: ", y_1)

    # Predict
    X_grid = np.arange(min(x_test), max(x_test), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    y_1 = regr_1.predict(X_grid)
    y_2 = regr_2.predict(X_grid)
    y_3 = regr_3.predict(X_grid)

    # Plot the results
    #plt.figure()
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, 1, 0.1))
    ax.set_yticks(np.arange(0, 1., 0.1))
    plt.scatter(x_test, y_test, s=20, edgecolor="black",
                c="dimgrey", label="Data")
    #linear regression plot
    plt.plot(X_grid, y_1,linestyle='-', color="black",
             label="Linear Regression", linewidth=2)
    #random forest plot
    plt.plot(X_grid, y_2,linestyle='--', color="black", label="Random Forest Regression", linewidth=2)
    #KnN-plot
    plt.plot(X_grid, y_3, linestyle=':', color="black", label=" K-Nearest Neighbor Regression", linewidth=2)

    plt.title(titel)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.legend()
    #plt.show()

    #plt.xticks(())
    #plt.yticks(())

    plt.grid()
    plt.show()




def main():
    y='revenue'
    y_label='Intäkter'
    x='actor'
    x_label='Engelska-Wikipedia Sidvisningar'
    titel=x_label
    #datasets = movie_object()     #import list with movieobjects
    cross_vali("new.csv",y,x,2,titel, y_label,x_label)
    #linear_regression(x_train,y_train,x_test,y_test,y,x)

if __name__ == '__main__':
    main()
