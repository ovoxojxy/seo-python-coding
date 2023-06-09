#!/usr/bin/python3
'''This mod is to write a function that returns True
if the object is an instance of a class that inherited
f_r_o_m the specified class; otherwise False'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a
    class that inherited f_r_o_m the specified class;
    otherwise False'''
    return isinstance(obj, a_class)
