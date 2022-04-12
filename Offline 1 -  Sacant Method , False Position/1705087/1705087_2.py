# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:08:21 2019

@author: FAHMID 1705087
"""

#import math 
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return (400*((x/(1-x))**2)*(6/(2+x)))**(1/2)-1
   
def yGenaratoRange(a):
    
    b=[]
    for element in a:
         b.append(f(element))
    return b

x=np.arange(0,1,.1)
y=yGenaratoRange(x)

with plt.style.context(('classic')):
    plt.plot(x,y,label='ln(1+x)', marker='o', markerfacecolor='blue', markersize=5, color='skyblue')
    

def falsePosition(function , lowerBound , upperBound, expRAerror, max_iteration):
    if f(lowerBound)*f(upperBound)>=0 :
        print("You have not assumed right lower and upper ")
        return -1
    nextTemp= lowerBound
    count=0
    
    while f(nextTemp) and count<max_iteration:
        count+=1
        
        prevTemp=nextTemp
        
        if (f(upperBound) - f(lowerBound))==0:
            print ("F zero divission error")
            break 
        
        nextTemp = (lowerBound * f(upperBound) - upperBound * f(lowerBound))/ (f(upperBound) - f(lowerBound))
        
        if abs(100*(nextTemp-prevTemp)/nextTemp)<expRAerror :
            break
        '''
        print("F Root = ",nextTemp)
        print("F error= ",abs(100*(nextTemp-prevTemp)/nextTemp))
        '''
        if f(nextTemp)*f(lowerBound)>=0:
            lowerBound=nextTemp
        else:
            upperBound=nextTemp
            
    print ("The number of iretation False Position = " ,count)
    return nextTemp

def secantMethod(function , InitialGuess1, InitialGuess2, expRAerror, max_iteration):
    count=1
    
    while count<max_iteration and abs(100*(InitialGuess2-InitialGuess1)/InitialGuess2)>expRAerror:
        count+=1
        
        if (f(InitialGuess2) - f(InitialGuess1))==0:
            print ("S zero divission error")
            break
        
        nextTemp = InitialGuess2 - ( (f(InitialGuess2) * (InitialGuess2 - InitialGuess1)) / (f(InitialGuess2) - f(InitialGuess1)) )
        InitialGuess1=InitialGuess2
        InitialGuess2=nextTemp
        '''
        print("S Root = ",nextTemp)
        print("S error= ",abs(100*(InitialGuess2-InitialGuess1)/InitialGuess2))
        '''
    print ("The number of iretation Secand Method= " ,count)
    return nextTemp

print ("The value of root with False Position = " ,falsePosition(f,0,.5,0.5, 1000000) )
print ("The value of root with Secand Method = " ,secantMethod(f,0,.5,0.5, 1000000) )

