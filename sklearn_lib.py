# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:07:26 2020

@author: Rashmi Thekkath
"""
import pandas as pd
masses_data = pd.read_csv('mammographic_masses.data.txt', na_values=['?'], names = ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity'])
masses_data.loc[(masses_data['age'].isnull()) |
              (masses_data['shape'].isnull()) |
              (masses_data['margin'].isnull()) |
              (masses_data['density'].isnull())]
masses_data.dropna(inplace=True)
masses_data.describe()
all_features = masses_data[['age', 'shape',
                             'margin', 'density']].values


all_classes = masses_data['severity'].values

feature_names = ['age', 'shape', 'margin', 'density']

#SKLEARN FOR PREPROCESSING
from sklearn import preprocessing
scaler = preprocessing.StandardScaler() 
#StandardScaler adjusts the data such that their mean is 0 and std deviation is 1
all_features_scaled = scaler.fit_transform(all_features)
print("All features scaled-")
print(all_features_scaled)
print("")

#SKLEARN FOR MODEL FITTING AND CROSS VALIDATION
from sklearn import neighbors #sklearn for K nearest neighbors algo
from sklearn.model_selection import cross_val_score #sklearn for cross validation score

clf = neighbors.KNeighborsClassifier(n_neighbors=10)
cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)

print("CV Scores-")
for n in range(1, 50):
    clf = neighbors.KNeighborsClassifier(n_neighbors=n)
    cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
    print (n, cv_scores.mean())