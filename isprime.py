# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:37:41 2021

@author: Mostafa
"""

def isprime(n):
    
    file=open('primes_database.txt','r+')
    temp=file.read()
    file.close()
    
    temp=temp.rstrip().split('\n')
    list_of_primes=[int(p) for p in temp]
    
    max_prime=list_of_primes[-1]
    
    if n>max_prime**2:
        raise ValueError('n must be less than {}.'.format(max_prime**2))
    
    for p in list_of_primes:
        
        if p>n**0.5:
            break
        
        if n/p==int(n/p):
            return False
    
    return True

if __name__=='__main__':
    print(isprime(117235504017087))