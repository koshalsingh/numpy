#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 00:02:57 2019

@author: koshal
                        Fancy Indexing              """
                        
a1=np.random.randint(0,20,15) 
print('Random matrix A : ', a1)

#filter even nums
mask = (a1%2==0)

#mask contains only boolean values
print('\nmask: ', mask)

#masking the A
even = a1[mask] 
print('\nextracting Even nums from a1: ', even)              

'''Remark:  Mask creates views not copies      '''
#changing all even values to -1
a1[mask]=-1
print('\nNew a1 : ',a1)

#accesing multiple index of the matrix
print('\n2,3,2,4,5th index of a1: ',a1[[2,3,2,4,5]])

#assinging the values to multiple indices
a1[[9,7]]=-200
print('\n again a1 : ', a1)