#*+-*+-!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:28:37 2019

@author: koshal
"""
#numpy 1
import numpy as np

#creating an array
lst=[1,2,3,4,5,6,7,8,9,10]
a1=np.array(lst)
print('array 1 is : ',a1)

a2=np.array([[7,8,9],[10,11,12]])
print('array 2 is : ',a2)
print()

#dimensiom
print('Dimension of array 1 is ',a1.ndim)
print('Dimension of array 2 is ',a2.ndim)
print()

#shape
print('Shape of  array 1 is ',a1.shape)
print('Shape of  array 2 is ',a2.shape)
print()

#length
print('Length of  array 1 is ',len(a1))
print('Length of  array 2 is ',len(a2))

'''             data types           '''
#show the data type of different matrices
print('\nThe datatype of a1 is : ', a1.dtype)

#providing datatype externally i.e. float64
a3=np.arange(10,dtype='float64')
print('\nthe matrix a3 is')
print(a3)
print('\nThe datatype of a3 is : ',a3.dtype)

print('\nNote: The default datatype of zeroes and ones is float64')


'''            Indexing ad slicing           '''
#accesing the 1-D matrix
print('\n A 1-D matrix:')
print(a1)
print('\nThe 3rd element is : ', a1[2])

#accesing the 2-D matrix
print('\n A 2-D matrix:')
print(a2)
print('\nThe 3rd element of 2nd row is : ', a2[1,2])

#Assigning a value in 2-D matrix
a2[1,2]=50
print('\nThe 3rd element of 2nd row is : ', a2[1,2])

#slicing from 1-D
s1=a1[1:10:2]
print('\nSliced only 1 to 9th index (only even idices)')
print(s1)

#slicing and assinging
#method 1
a1[5:10]=[10,11,12,13,14]
print('\n New a1 ', a1)
#method2
a1[5:10]=999
print('\n New a1 ', a1)
#method3
a4=np.arange(5)
a1[5:10]=a4[::-1]
print('\n New a1 ', a1)