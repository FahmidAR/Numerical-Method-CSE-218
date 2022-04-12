# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:04:31 2019

@author: FAHMID 1705087
"""

def lnOnePlus(x,n):
    
    sum=0.0
    term=x
    
    for element in range(1,n+1):

        sum+=float(term)/element
        term*=(-1)*x
        
    return sum

def yGenaratoRange(a,n):
    
    b=[]
    for element in a:
        
      b.append(lnOnePlus(element,n))
    return b
    
import math
import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-1,1,.1)
y=np.log(1+x)


a=yGenaratoRange(x,1)
b=yGenaratoRange(x,3)
c=yGenaratoRange(x,5)
d=yGenaratoRange(x,20)
e=yGenaratoRange(x,50)

with plt.style.context(('classic')):
    plt.plot(x,y,label='ln(1+x)', marker='o', markerfacecolor='blue', markersize=5, color='skyblue')
    plt.plot(x,a,label='ln(1+x) n=1')
    plt.plot(x,b,label='ln(1+x) n=3')
    plt.plot(x,c,label='ln(1+x) n=5')
    plt.plot(x,d,label='ln(1+x) n=20')
    plt.plot(x,e,label='ln(1+x) n=50')

    plt.legend(loc='lower right')
    plt.grid(color='white',linewidth=1,linestyle='-')
    plt.xlabel("X values ")
    plt.ylabel(" ln(1+x) Funtion values")
    plt.title("Natural logarithm function graph")

plt.figure() 

term=np.arange(1,50,1)
error=[]

'''
for i in term:
    error.append(math.fabs(math.log(1.5)-lnOnePlus(.5,i))/math.log(1.5))
'''

for i in term:
    error.append(math.fabs(lnOnePlus(.5,i)-lnOnePlus(.5,i-1))/lnOnePlus(.5,i))


with plt.style.context('seaborn'):
    plt.plot(term,error,label='ln(1+x)', marker='o', markerfacecolor='blue', markersize=2, color='skyblue')
    plt.legend(loc='lower right')
    plt.grid(color='white',linewidth=1,linestyle='-')
    plt.xlabel("terms no ")
    plt.ylabel(" relative error")
    plt.title("Error calculations graph")

input1=input("Enter the value of x:")
input2=input("Enter the iteration number:")

print(input1,input2)
print ("The value of ln(1+x) = ",lnOnePlus(float(input1),int(input2)))
print("\n")