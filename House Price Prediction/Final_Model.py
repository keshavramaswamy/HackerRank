# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 01:52:10 2014

@author: HP
"""
import numpy as np

str = raw_input()

strl = str.split()

num_feat = int(strl[0])

num_rows = int(strl[1])

f1 = open("train.txt", "w")

for i in range(num_rows):
    line = raw_input()
    linel = line.split()
    for j in range(num_feat+1):
        #k = int(linel[j])
        f1.write(linel[j])
        f1.write(" ")
    f1.write("\n")
    
f1.close()

num_test = int(raw_input())

f2 = open("test.txt", "w")

for i in range(num_test):
    line = raw_input()
    linel = line.split()
    for j in range(num_feat):
        #k = int(linel[j])
        f2.write(linel[j])
        f2.write(" ")
    f2.write("\n")
    
f2.close()




num_feat =2 
data1 = np.loadtxt('train1.txt')
x= data1[:,[0,num_feat-1]]
y= data1[:,num_feat]

data2 = np.loadtxt('test1.txt')
z = data2[:,[0,num_feat-1]]




from sklearn import linear_model
clf = linear_model.LinearRegression()

clf.fit (x,y)
coef = clf.coef_

prod = np.dot(z,coef)

ans = prod + clf.intercept_
for i in ans:
    print i        
