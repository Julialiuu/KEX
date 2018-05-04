import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold
import csv
from math import sqrt
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


def cross_vali(csv_file,y_header,x_header, number_of_splits,titel):
    df=pd.read_csv(csv_file)
    df = df[df[x_header] != 0]
    y=df[y_header]
    y=y.reshape(len(y),1)

    x = df[x_header]
    x=x.reshape(len(x),1)


    #split the trainingdata and testdata
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

    #create linear regression object
    regr = KNeighborsRegressor()
    error =  []
    coeficient = 0
    MAE = 0
    MSE = 0
    Root_MSE = 0
    r2 = 0

    regr = linear_model.LinearRegression()
    # train the model using the training sets
    regr.fit(x_train,y_train)
    # make predictions using the testing sets
    prediction = regr.predict(x_test)
    coeficient = regr.coef_
    MAE = mean_absolute_error(y_test, prediction)
    MSE = mean_squared_error(y_test, prediction)
    Root_MSE = np.sqrt(mean_squared_error(y_test, prediction))
    r2 = r2_score(y_test, prediction)

    # The coefficients
    print('Coefficients:', coeficient)
    #the mean squared error
    print('Mean Absolute Error:', MAE)
    print('Mean Squared Error:', MSE)
    print('Root Mean Squared Error:', Root_MSE)
    print("r2_score:", r2)

    # plot outputs
    plt.scatter(x_test,y_test, color='black')
    plt.plot(x_test,prediction,color='red',linewidth=3)
    #plt.scatter(prediction,color='red')
    #plt.scatter(y_test,color='blue')
    #print("P: ", y_test)

    plt.title(titel)
    plt.ylabel(y_header)
    plt.xlabel(x_header)

    plt.xticks(())
    plt.yticks(())

    plt.show()




def main():
    y='revenue'
    x='production_budget'
    titel='K-nearest neighbors'
    #datasets = movie_object()     #import list with movieobjects
    cross_vali("new.csv",y,x,2,titel)
    #linear_regression(x_train,y_train,x_test,y_test,y,x)

if __name__ == '__main__':
    main()
