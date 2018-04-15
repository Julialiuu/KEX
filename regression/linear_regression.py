import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv
import pandas as pd
#from movie_object import movie_object

def cross_vali():
    df=pd.read_csv("out_headers.csv")

    y=df['revenue']
    x=df['imdb_rating']

    x=x.reshape(len(x),1)
    y=y.reshape(len(y),1)

    x_train=x[:-250]
    y_train=y[:-250]

    x_test=x[-250:]
    y_test=y[-250:]

    plt.scatter(x_test,y_test, color='black')
    plt.title('test data')
    plt.ylabel('revenue')
    plt.xlabel('imdb rating')
    plt.xticks(())
    plt.yticks(())


    regr = linear_model.LinearRegression()

    regr.fit(x_train,y_train)

    plt.plot(x_test,regr.predict(x_test),color='red',linewidth=3)
    plt.show()

def main():
    #datasets = movie_object()     #import list with movieobjects
    cross_vali()

if __name__ == '__main__':
    main()
