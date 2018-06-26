# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:18:26 2018

@author: Mauricio.Cordero

Description: Script to display text classification functionality and strategy.
Separates the training of the classifier from its potential usage in production
for classifying text. Displays ability to train model offline while using pre-
trained classifiers in production.
"""

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from sklearn.base import BaseEstimator
from albclf.exceptions import PickleError


def trainClassifier(data, clf_name):  
    albert_clf = Pipeline([('vect', CountVectorizer()),
                           ('tfidf', TfidfTransformer()),
                           ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                 alpha=1e-3, random_state=42,
                                                 max_iter=5, tol=None))
                          ])
                          
    parameters = {
                  'vect__ngram_range': [(1, 1), (1, 2)],
                  'tfidf__use_idf': (True, False),
                  'clf__alpha': (1e-2, 1e-3),
                 }
    gs_clf = GridSearchCV(albert_clf, parameters, n_jobs=1, cv=3)
    # Must set n_jobs=1 because n_jobs!=1 breaks from Spyder, but works from Jupyter!
    
    gs_clf.fit(data.Message, data.Category)
    
    best_estimator = gs_clf.best_estimator_
    joblib.dump(best_estimator, clf_name)
    
    return best_estimator
   
     
def loadClassifier(pickled_clf):
    try:
        classifier = joblib.load(pickled_clf)
        
        if isinstance(classifier, BaseEstimator):
            print("Loading saved classifier...")
            return classifier
        else:
            print("Invalid classifier loaded; training new one.")
            raise PickleError("Invalid classifier loaded.")
            
    except IOError:
        # File not found; train a new classifier
        print("No existing classifier found; training new one.")
        raise PickleError("No exisiting classifier found.")
        
        
def predict(classifier, message):
        try:
            result = classifier.predict([str(message)])
            category = result[0]
        except (IndexError, AttributeError):
            category = 'Invalid result' 

        return category    