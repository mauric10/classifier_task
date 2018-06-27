# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:30:24 2018

@author: Mauricio.Cordero
"""


class DataError(Exception):
    """ Exception for errors associated with non-standard or non-existing
    training data.
    """
    def __init__(self, message):
        self.message = message


class PickleError(Exception):
    """
    """
    def __init__(self, message):
        self.message = message
