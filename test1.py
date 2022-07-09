# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:44:08 2022

@author: smosaya
"""

import numpy as np


def generateRandomNumbers(m,n):
    s="0,1,2,3,4,5,6,7,8,9".split(",")
    
    while 1:
        x="".join(np.random.choice(s,m))
        y="".join(np.random.choice(s,n))
        if not x[0]=="0" and not y[0]=="0":
            return x,y

# def charAsDigit(c):
#     return int("c")

def modulo(x,y):
    
    numOfXDigits=len(x)
    numOfYDigits=len(y)
    
    # print(numOfYDigits-numOfXDigits)
    
    z=x[:numOfXDigits-numOfYDigits+1]
    
    print(z)
    
    return 1
#%%
if __name__=="__main__":
    
    x,y=generateRandomNumbers(10, 5)
    
    print(x)
    print(y)
    
    modulo(x, y)