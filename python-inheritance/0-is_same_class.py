#!/usr/bin/python3
'''This mod conatins a function that returns true if the object is 
exactly an instance of the specified class; otherwise False'''


def is_same_class(obj, a_class):
    '''this is the function referenced in the above doc'''
    return(type(obj) == a_class)
