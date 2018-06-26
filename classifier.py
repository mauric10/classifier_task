# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:18:26 2018

@author: Mauricio.Cordero

Description: Script to display text classification functionality and strategy.
Separates the training of the classifier from its potential usage in production
for classifying text. Displays ability to train model offline while using pre-
trained classifiers in production.
"""

import sys
import pandas as pd
from sklearn.base import BaseEstimator
from albclf.exceptions import DataError, PickleError
from albclf.utils import trainClassifier, loadClassifier, predict


def main():
    try:
        message = sys.argv[1]
    
    except IndexError:
        print("Message for classification task not passed.")
        return
    
    if len(sys.argv) > 2:
        print("Too many msgs passed.")
        return
    
    else:
        try:
            # try to load saved classifier
            classifier = loadClassifier('classifier.pkl')
            
        except PickleError:
            # if no saved classifier found, train a new one with data provided.
            try:
                data = pd.read_csv('data/ProjectTrainingData.csv')
                if "Message" and "Category" not in data.keys():
                    raise DataError
                    
            except IOError:
                print('Training data not found. Stopping program.')
                return
                
            except DataError:
                print('Incorrectly formatted data. Stopping program.')
                return
        
            # finally train (& save) classifier if not loaded above and data is OK        
            classifier = trainClassifier(data, 'classifier.pkl')  
        
        if isinstance(classifier, BaseEstimator):            
            category = predict(classifier, message)
            print("Returned category: %s" % category)
        
        else:
            print("Non-classifier returned. Stopping program.")


def test_main():
    sys.argv = sys.argv[:1]
    sys.argv.append('This is a financial question.')
    return main()


if __name__ == "__main__":
    main()