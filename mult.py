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
#from movie_object import movie_object


def cross_vali(csv_file,y_header,x_header):
    df=pd.read_csv(csv_file)

    y=df[y_header]
    print(y)
    y=y.reshape(len(y),1)


    x = np.array([df['production_budget'], df['imdb_rating']])
    #x = np.array([df['production_budget'], df['imdb_rating'],df['wiki_en'],df['wiki_sv'],df['sf_rating']])
    x = x.transpose()


    #split the trainingdata and testdata
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    print(y)

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
    plt.plot(x_test,prediction,color='red',linewidth=3)

    plt.title('Test Data')
    plt.ylabel(y_header)
    plt.xlabel(x_header)

    plt.xticks(())
    plt.yticks(())

    plt.show()


def main():
    y='revenue'
    x='production_budget'
    #datasets = movie_object()     #import list with movieobjects
    [x_train,y_train,x_test,y_test]=cross_vali("production_budget_imdb.csv",y,x)
    linear_regression(x_train,y_train,x_test,y_test,y,x)

if __name__ == '__main__':
    main()
