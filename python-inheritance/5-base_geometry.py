#!/usr/bin/python3
'''This modules purpose is to write a class 
based on the previous class with public instance
area(self)'''


class BaseGeometry:
    '''Class with private width and height instantiations'''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
	    raise TypeError(f'{name} must be an integer')
	if values<= 0;
	    raise ValueError(f'{name} must be greater than 0')
