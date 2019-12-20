#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:42:26 2019

@author: koshal
"""
#numpy 2
import numpy as np
'''            creating different types of array using numpy '''
#creating an array
lst=[1,2,3,4,5,6]
a1=np.array(lst)
print('array 1 is : ',a1)

a2=np.array([[7,8,9],[10,11,12]])
print('array 2 is : ',a2)

a3=np.arange(10)
print('array 3 is :', a3)
a4=np.arange(0,10,2)
print('even no.s array : ', a4)
print()

#linespace
a5=np.linspace(1,10,10)
print('10 partition between 1 to 10 ', a5)
print()

#matrix with only ones
a6=np.ones((3,3))
print('3*3 matrix with only one')
print(a6)
print()

#matrix with only zeroes
a7=np.zeros((3,3))
print('3*3 matrix with only zeros')
print(a7)
print()

#identity matrix
a8=np.eye(3,3)
print('Identity matrix with diagonal 1: ')
print(a8)
print()

#Diagonal matrix
a9=np.diag([1,2,3,4])
print('Matrix with diagonal 1,2,3,4')
print(a9)
print()

#extracting the diagonal of the above matrix
d1=np.diagonal(a9)
print('the diagonal of the above Matrix is :')
print(d1)
print()

aa1=np.eye(3,2)
print(aa1)
d2=np.diagonal(aa1)
print('the diagonal of the above Matrix is :')
print(d2)