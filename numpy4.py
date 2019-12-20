#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:12:56 2019

@author: koshal
                Copies and values               """
                
a1=np.arange(10)
print('a1 : ', a1)
b1=a1[::2]
print('b1 = a1[::2] : ', b1)

#check whether a1 and b1 shares the same memory allocation
print('\nDoes a1 and b1 share the same memory allocation :')
print(np.shares_memory(a1,b1))                

b1[1]=999
print('\nlets change b1[1]=999')
print('b1', b1)
print('a1', a1)
print('changing the value of b1, value of a1 is automaticaly changed')

a2=np.arange(10)
print('\na2 : ',a2)
print('Does a1 and a2 share the same memory allocation :')
print(np.shares_memory(a1,a2)) 

#making copies without sharing the memories
c1=a1[::2].copy()
print('\n c1=a1[::2].copy() ', c1)
print('Does a1 and c1 share the same memory allocation :')
print(np.shares_memory(a1,c1))

#changing the value of c1 for testing 
c1[1]=2
print('\nlets change c1[1]=1')
print('c1', c1)
print('a1', a1)
print('changing the value of c1, value of a1 is not changed')

