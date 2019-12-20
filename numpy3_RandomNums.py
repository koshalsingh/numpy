#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:11:38 2019

@author: koshal
                    creating matrix with Random Numbers      """
                    
import numpy as np

#creating a matrix with random numbers between 0 to 1(floating points)
r1=np.random.rand(3,3)
print('3*3 matrix with range 0 to 1 floating points')
print(r1)
print()

#creating 3*3 matrix with random numbers between 1 to 6 
r2=np.random.randint(1,7,(3,3))
print('3*3 matrix with range 1 to 6 (integers)')
print(r2)
print()

