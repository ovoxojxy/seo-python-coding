#!/usr/bin/python3
'''This mod creates a function that returns true or false 
depending on whether the obj is from the same instance as\
the object in the functions argument or not'''
def is_kind_of_class(obj, a_class):
'''This function returns true if an object is the same instanc
as the class argument'''
    return(type(obj) == a_class)
