# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:39:26 2024

@author: moon
"""
# global result
result = 0
def add(num):
    global result 
    result = result + num
    return result
print(add(3))
result
print(add(4))
# result

#%%
def add(num):
    result = 0
    result = result + num
    return result
print(add(3))
result
print(add(4))
# result