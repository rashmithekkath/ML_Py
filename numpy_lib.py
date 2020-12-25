# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:29:59 2020

@author: Rashmi Thekkath
"""
import numpy as np

arr = np.array( [[ 'my', 'first', 'try'], 
                 [ 'a', 'b', 'c']] ) 
   
print("Dimensions-", arr.ndim)  #array_name.ndim for array dimensions
print("Shape-", arr.shape) #array_name.shape for shape of array
print("Size of array-", arr.size) #array_name.size for total number of elements 
print("Element type: ", arr.dtype) #array_name.dtype for type of elements in array
print("Array type: ", type(arr)) #type(array_name) for type of array
print("")

zero_arr = np.zeros((2, 4)) #array created of size 2x4 with all 0 values
print("Zero array")
print(zero_arr)
print("")

random_arr = np.random.random((2,2)) #array created of size 2x2 with random values
print("Random Array")
print(random_arr)
print("")

sequence = np.arange(0, 20, 4) #creates as a sequence from 0 to 20 with a step of 4
print(f"sequence- {sequence}")
print("")

linspace_seq = np.linspace(0, 5, 10) #creates a sequence of 10 numbers between 0 and 5
print("Linspace Array")
print(linspace_seq)
print("")

int_arr = np.array([[1,3,5],[2,4,6]], dtype="int")
arr_flattened = int_arr.flatten() #array_name.flatten() to flatten the array
print("Flattened array")
print(arr_flattened)
print("")

arr1 = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9],
                [10,11,12]]) 
newarr = arr1.reshape(3, 4) #Reshaped array to size arr_size of 3,4
print(newarr) 