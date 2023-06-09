#!/usr/bin/python3
'''THis mod has a class BaseGeometry based on 3-base_geometry.py'''


class BaseGeometry:

    '''This class has a public instance method: def are(self):
    That raises an Exception with the message area() is not
    implemented'''
    def area(self):
	raise Exception('area() is not implemented')
