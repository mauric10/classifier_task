# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:53:15 2018

@author: Mauricio.Cordero
"""
from albclf.utils import trainClassifier, loadClassifier, predict
from sklearn.externals import joblib
from sklearn.base import BaseEstimator
from albclf.exceptions import PickleError
import pandas as pd


def testLoadClassifierProperly():
    clf = loadClassifier('classifier.pkl')
    assert isinstance(clf, BaseEstimator)

def testLoadClassifierCorrupt():
    try: 
        clf = loadClassifier('')
    except PickleError:
        assert True
    
def testTrainClassifierBadData():
    try:
        df = pd.DataFrame.from_dict({'Message': ['This is financial question.'],
                                     'Category': ['debt']}, orient='columns')
        for i in range(1, 50):
            df.ix[i] = df.ix[i-1]
            
        clf = trainClassifier(df, 'test.pkl')
    except ValueError as e:
        assert e.message == 'The number of class labels must be greater than one.'
    
def testTrainClassifierGoodData():   
    df = pd.DataFrame.from_dict({'Message': ['This is financial question.'],
                                 'Category': ['debt']}, orient='columns')
    for i in range(1, 50):
        df.ix[i] = df.ix[i-1]   

    df.ix[10:19].Category = 'savings'
    df.ix[20:29].Category = 'finance'
    df.ix[30:39].Category = 'technical'
    df.ix[40:49].Category = 'account'
    
    clf = trainClassifier(df, 'tests/test.pkl')
    assert isinstance(clf, BaseEstimator)
        
def testPredict():
    clf = joblib.load('classifier.pkl')
    result = predict(clf, 'This is a financial question.') 
    assert isinstance(result, str) 
    

    