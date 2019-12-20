#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 00:20:38 2019

@author: koshal
                operations on numpy array"""
import numpy as np
a1=np.array([1,2,3,4])
print('matrix 1 is :', a1)

print('\nAdding 1 to all elements i.e. b1=a1+1')
b1=a1+1 #adding 1 to all elemnts of a1
print('Matrix 2 is :',b1)

print('\nSubtracting 1 from all elements i.e. b2=a1-1')
b2=a1-1 #subtracting 1 from all elemnts of a1
print('Matrix 3 is :',b2)

print('\nMultiplying 2 to all elements i.e. b2=a1*2')
b3=a1*2 #Multiplying 1 from all elemnts of a1
print('Matrix 4 is :',b3)

print('\nMultiplying a1 and b3,   b4=a1*b3')
b4=a1*b3 #Multiplying a1 and b3,   b4=a1*b3
print('Matrix 5 is :',b4)

print('\nfind dot product of two matrices')
c1=np.diag([1,2,3,4])
c2=np.diag([2,3,4,5])
print('\nMatrix c1 is :')
print(c1)
print('\nMatrix c2 is :')
print(c2)
#Dot product
dot1=np.dot(c1,c2)
print('\nMatrix c1.c2 is :')
print(dot1)
dot2=c1*c2
print('\nMatrix c1*c2 is :')
print(dot1)
print('Remark: c1*c2 is same as c1.c2')

#comparision using == operator, which return boolean values
print('\n         Illustration of == operator')
a2=np.array([1,2,3,4])
a3=np.array([5,2,3,6])
print('\nMatrix a2 :')
print(a2)
print('\nMatrix a3 :')
print(a3)

print('\nIs a2==a3 : ', a2==a3)
print('Hence we can conclude that == compares the array element-wise')

#comparing the array
a4=np.array([1,2,3,4])
print('\nMatrix a2 : ', a2)
print('\nMatrix a3 : ', a3)
print('\nMatrix a4 : ', a4)

'''         comparing arrays using array_equal(a,b)   '''
print('\nIs a2 equals to a3 : ',np.array_equal(a2,a3))
print('\nIs a2 equals to a3 : ',np.array_equal(a2,a4))
print('\nIs a2 < a3 : ', a2<a3)

'''         Logical Operator            '''
b5=np.array([1,1,0,0], dtype=bool)
b6=np.array([1,0,1,0], dtype=bool)
print('\nMatrix b5 : ',b5)
print('\nMatrix b6 : ', b6)
print('\nnp.logical_or(b5,b6) : ', np.logical_or(b5,b6))
print('\nnp.logical_and(b5,b6) : ', np.logical_and(b5,b6))

'''             Transcendental Functions        '''
s1=np.array([1,2,3,4,5,6,7,8,9,10])
print('\n\ns1 : ', s1)
print('np.sin(s1) : ', np.sin(s1))
print('\nnp.log(s1) : ', np.log(s1))
