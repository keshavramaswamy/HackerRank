# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 09:24:20 2015

@author: HP
"""

def calc_count(input):
    count_a = 0
    count_an = 0
    count_the = 0
    #count_date = 0
    for iter in input.split():
        if iter == 'a':
            count_a += 1
        if iter == 'an':
            count_an += 1
        if iter == 'the':
            count_the += 1
            
    print count_a,count_an,count_the
    
str = raw_input()

print str.split()


        
    
    
    
    
    
    
    
    
    
    
    
'''  

var_t = int(raw_input())

list_frag =[]

for iter in range(2*var_t):
    str = raw_input()
    if (str!=''):
        list_frag.append(str)
        
for iter in list_frag:
    count_a,count_an,count_the,count_date = calc_count(iter)
    

'''