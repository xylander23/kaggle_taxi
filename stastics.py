#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

def loaddata(trainpath,testpath):
    traindata = pd.read_csv(trainpath)
    testdata = pd.read_csv(testpath)
    print 'completed load'
    return traindata,testdata
    
def viewdata(train,test):
    print train.describe()
    print test.describe()
    
def removeoutline(train):
    #剔除异常数据
    m = np.mean(train['trip_duration'])
    v = np.std(train['trip_duration'])
    train = train[train['trip_duration'] <= m + 2*v]
    train = train[train['trip_duration'] >= m - 2*v]
    #print train.info()
    #剔除非纽约地区数据
    train = train[train['pickup_longitude'] <= -73.75]
    train = train[train['pickup_longitude'] >= -74.03]
    train = train[train['pickup_latitude'] <= 40.85]
    train = train[train['pickup_latitude'] >= 40.63]
    train = train[train['dropoff_longitude'] <= -73.75]
    train = train[train['dropoff_longitude'] >= -74.03]
    train = train[train['dropoff_latitude'] <= 40.85]
    train = train[train['dropoff_latitude'] >= 40.63]
    #选取人数大于0小于5的
    train = train[train['passenger_count'] > 0]
    train = train[train['passenger_count'] <= 5]
    return train

def dateform(train,test):
    train['pickup_datetime'] = pd.to_datetime(train.pickup_datetime)
    test['pickup_datetime'] = pd.to_datetime(test.pickup_datetime)
    train.loc[:,'pickup_date'] = train['pickup_datetime'].dt.date
    test.loc[:,'pickup_date'] = test['pickup_datetime'].dt.date
    train['dropoff_datetime'] = pd.to_datetime(train.dropoff_datetime)

def plotcountnumber(train):
    plt.hist(train.trip_duration,bins='auto')
    plt.xlabel('trip_duration')
    plt.ylabel('frequence')
    plt.show()
    plt.hist(np.log(train.trip_duration),bins='auto')
    plt.xlabel('trip_duration')
    plt.ylabel('log of frequence')
    plt.show()
    
def plotdatacount(train,test):
    plt.plot(train.groupby(train['pickup_date']).count()[['id']],'o-',label='train')
    plt.plot(test.groupby(test['pickup_date']).count()[['id']],'o-',label='test')
    plt.show()
    
if __name__ == '__main__':
    print 'data mining'
    trainpath = 'E:/Kaggle/taxi/data/train/train.csv'
    testpath = 'E:/Kaggle/taxi/data/test/test.csv'
    train,test = loaddata(trainpath,testpath)
    #viewdata(train,test)
    train = removeoutline(train)
    dateform(train,test)
    #plotcountnumber(train)
    plotdatacount(train,test)
    
    
    