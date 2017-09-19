# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:02:46 2016

@author: enbody
"""

L1 = [8,5]
L2 = [3, L1, 2]
print(L2)  # Line 1
L1[0] = 7
print(L2)  # Line 2
L2.append("X")
print(L2)  # Line 3

L3 = [1,2]
L4 = ['a','b']
L3.append(L4)
print(L3)
L3 = [1,2]
L3.extend(L4)
print(L3)