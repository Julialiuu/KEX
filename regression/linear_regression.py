import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#from movie_object import movie_object


def cross_vali(csv_file,y_header,x_header):
    df=pd.read_csv(csv_file)

    y=df[y_header]
    x=df[x_header]

    x=x.reshape(len(x),1)
    y=y.reshape(len(y),1)

    x_train=x[:-100]
    y_train=y[:-100]

    x_test=x[-100:]
    y_test=y[-100:]
    return [x_train,y_train,x_test,y_test]

def linear_regression(x_train,y_train,x_test,y_test,y_header,x_header):

    #create linear regression object
    regr = linear_model.LinearRegression()
    # train the model using the training sets
    regr.fit(x_train,y_train)
    # make predictions using the testing sets
    prediction= regr.predict(x_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    #the mean squared error
    print('Mean squared error: %.2f'
        % mean_squared_error(y_test,prediction))

    # plot outputs
    plt.scatter(x_test,y_test, color='black')
    plt.plot(x_test,prediction,color='red',linewidth=3)

    plt.title('Test Data')
    plt.ylabel(y_header)
    plt.xlabel(x_header)

    plt.xticks(())
    plt.yticks(())

    plt.show()

def main():
    y='revenue'
    x='imdb_rating'
    #datasets = movie_object()     #import list with movieobjects
    [x_train,y_train,x_test,y_test]=cross_vali("imdb_rating.csv",y,x)
    linear_regression(x_train,y_train,x_test,y_test,y,x)

if __name__ == '__main__':
    main()
