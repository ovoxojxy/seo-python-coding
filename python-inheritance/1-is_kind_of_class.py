#!/usr/bin/python3
'''This mod creates a function that returns true if the object
is an instance of, or if the object is an instance of a class
that inherited from, the specified class; otherwise false'''


def is_kind_of_class(obj, a_class):
    '''Function returns true or false depending
    on if the object is from the same class as the
    other function argument'''
    return(type(obj) == a_class) or isinstance(obj, a_class)
