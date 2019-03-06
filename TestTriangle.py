# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    #right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    #equilateral triangles
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 should be equilateral')
    
    #isosceles triangles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,4), 'Isosceles', '3,4,4 should be isosceles')
    
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(6,5,6), 'Isosceles', '6,5,6 should be isosceles')

    #scalene triangles
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5,6,7), 'Scalene', '5,6,7 is scalene')
    
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(8,7,6), 'Scalene', '9,1,3 is scalene')

    #not valid test
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(5000,4000,3000), 'InvalidInput', 'Outside of 200 pt parameter')
    def testInvalidInputB(self):  
        self.assertEqual(classifyTriangle(5,-4,-3), 'InvalidInput', 'Two factors are negative')
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(3.5,4,3), 'InvalidInput', 'Invalid instance')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
