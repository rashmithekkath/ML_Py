# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:29:13 2020

@author: Rashmi Thekkath
"""

import numpy as np
from scipy import linalg #FOR LINEAR ALGEBRA

#To solve for a two unknown - two equation problem
#Ex. To solve for: 2x+5y=10 and 5x+3y=9
A= np.array([[2,5],[5,3]]) # Create input array i.e. LHS
B= np.array([[10],[9]]) #RHS or output array
X= linalg.solve(A,B) #Solve both equations linalg.solve(input_arr,output_arr)
print("Solution for 2 eq-2 var:")
print(X)
print("")


inverted_sqmatrix=linalg.inv(A)#scipy.linalg.inv() for Inverse of any square matrix
print("Inverted Square Matrix")
print(inverted_sqmatrix)
print("")

#find combinations of 6C4 values using comb(N, k)
#find permutation of 6P2 values using comb(N, k)
from scipy import special
combinations = special.comb(6,4, exact = False, repetition=False) 
print(f"Combination output: {combinations}" )
permutations = special.perm(6,2)
print(f"Permutation output: {permutations}" )

#SCIPY FOR CUBE ROOT
from scipy.special import cbrt
cb = cbrt([8, 1000])#Find cubic root of 8 & 1000 using cbrt() function
print(cb)

