import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import csv
from math import sqrt
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

#from movie_object import movie_object


def cross_vali(csv_file,y_header,x_header):
    df=pd.read_csv(csv_file)

    y=df[y_header]
    y=y.reshape(len(y),1)


    x = np.array([df['production_budget'], df['imdb_rating']])
    #x = np.array([df['production_budget'], df['imdb_rating'],df['wiki_en'],df['wiki_sv'],df['sf_rating']])
    x = x.transpose()


    #split the trainingdata and testdata
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

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


    print('Mean Absolute Error:', mean_absolute_error(y_test, prediction))
    print('Mean Squared Error:', mean_squared_error(y_test, prediction))
    print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, prediction)))

    r2=r2_score(y_test, prediction)
    print("r2_score:", r2)

        # plot outputs
    #plt.scatter(x_test,y_test, color='black')
    # plt.scatter(prediction,color='red')
    # plt.scatter(y_test,color='blue')
    # print("P: ", y_test)
    #
    # plt.title('Test Data')
    # plt.ylabel(y_header)
    # plt.xlabel(x_header)
    #
    # plt.xticks(())
    # plt.yticks(())
    #
    # plt.show()

    #ax = Axes3D(fig)

    x_vals = x_test[:,0]
    y_vals = x_test[:,1]
    z_vals = prediction

    xx, yy = np.meshgrid(x_vals, y_vals)

    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    surf=ax.plot_surface(x_vals, y_vals, z_vals)

    #plot the scatter
    #ax.scatter(x_vals, y_vals, z_vals)

    pyplot.show()


def main():
    y='revenue'
    x='production_budget'
    #datasets = movie_object()     #import list with movieobjects
    [x_train,y_train,x_test,y_test]=cross_vali("production_budget_imdb.csv",y,x)
    linear_regression(x_train,y_train,x_test,y_test,y,x)

if __name__ == '__main__':
    main()
