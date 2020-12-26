# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:55:55 2020

@author: Rashmi Thekkath
"""
import numpy as np
import pandas as pd

#PANDAS SERIES DATA STRUCTURE
import sys
sys.__stdout__ = sys.stdout 
#WITHOUT this command, it can show an error and not print the series o/p  
#cause- PANDAS looks for the amount of info to be displayed
#so sys output information should be explicitly mentioned

#Using NumPy Array
series_ = np.array(['first_element','second_element','third_element','fourth_element'])
series1 = pd.Series(series_) 
print(series1)
print("")

#Directly Using Pandas
series2 = pd.Series([11,22,33,44])
print(series2)
print("")

#PANDAS DATAFRAME 
df = pd.DataFrame({
    "Column1": ['val1_in_col1', 'val2_in_col1', 'val3_in_col1', 'val4_in_col1'],
    "Column2": [1,2,3,4],
    "Column3": ['val1_in_col3', 'val2_in_col3', 'val3_in_col3', 'val4_in_col3'],
    "Column4": [True, False, True, False]
})
print(df)
print("")


#DATA WRANGLING - CONCATENATION, GROUPING, MERGING
d1={'df_col1': ['1', '2', '3', '4', '5'],
    'df_col2': ['Everdeen', 'Mellark', 'Hawthorne', 'Katniss', 'Peeta']}
df1 = pd.DataFrame(d1)

d2={'df_col1': ['4', '5', '3', '8', '9'],
    'df_col2': ['Katniss', 'Mellark', 'Katniss', 'Peeta', 'Mellark']}
df2 = pd.DataFrame(d2)

print("After concatenation") 
print(pd.concat([df1,df2])) #pd.concat([df1,df2]) for concatenation
print("")
print(f"After Grouping in df2- {df2.groupby('df_col2')}")
print("")

group=df2.groupby('df_col2') #df_name.groupby("col_name") for grouping based on a column
print("From Grouped Data based on df_col2 values, extract Katniss values and corresponding columns" )
print(group.get_group('Katniss')) 
print("")

print(pd.merge(df1, df2, on='df_col2')) #pd.merge(df1,df2,on="col_based_on_which_merge")
print("")

#DESCRIPTIVE ANALYSIS 
print(df2.describe())


