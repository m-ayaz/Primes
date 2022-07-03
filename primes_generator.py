# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:03:10 2021

@author: Mostafa
"""

#import numpy as np
from tqdm import tqdm

try:
    file=open('primes_database.txt','r+')
except FileNotFoundError:
    file=open('primes_database.txt','w+')
    file.writelines("2\n3\n5")
    file.close()
    file=open('primes_database.txt','r+')
temp=file.read()
#file.close()

temp=temp.strip().split('\n')
list_of_primes=[int(p) for p in temp]

old_primes=list_of_primes.copy()

#print(temp)

#=1

base_prime=list_of_primes[-1]

x=base_prime+2

number_of_new_primes=int(input('Number Of New Primes : '))
#%%
#for _ in range(5000):
for _ in tqdm(range(number_of_new_primes),position=0,leave=True):
    
    prime_flag=1
    
    for p in list_of_primes.copy():
        
        if p>x**0.5:
            break
        
        if x/p==int(x/p):
            prime_flag=0
            break
    
    if prime_flag==1:
        list_of_primes.append(x)
    
    x+=2
#%%
#for p in list_of_primes:
for p in tqdm(list_of_primes,position=0,leave=True):
    if p>base_prime:
#        print(p)
        file.writelines(f'\n{p}')
file.close()