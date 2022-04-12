# -*- coding: utf-8 -*-
"""
*************************************************************
Created on Mon Aug  5 01:42:28 2019
@author: Fahmid_1705087
*************************************************************
"""

import math
import numpy as np
from matplotlib import pyplot as plt

'''
*************************************************************
Input taking from file 
Makig list with points
*************************************************************
'''
listAllNumber=[]
X=[]
Y=[]

flag=-1

with open("input.txt", "r+") as f:
    
    lines=f.readlines()
    for line in lines:
        listAllNumber+=line.strip().split(" ")

#print(listAllNumber)

for num in listAllNumber:
    
    if(flag==-1):
        n=int(num)
        flag=1
    elif(flag==1):
        X.append(float(num))
        flag=0
    else:
        Y.append(float(num))
        flag=1

#print(n)
#print(X)
#print(Y)
        
'''
*************************************************************
Sort X, Y
And Check
*************************************************************
'''

lenX=len(X)

for i in range(lenX): 
  
    for j in range(0,lenX-i-1):
        
        if X[j]>X[j+1]:
            
            X[j], X[j+1] = X[j+1], X[j]
            Y[j], Y[j+1] = Y[j+1], Y[j]
            

#print(X)
#print(Y)
            
'''
*************************************************************
Numerical Integration funtions  for same Ineterval Points
Sove funtion 
*************************************************************
'''

def trapezoidal(X,Y,first,last,interval_value):
    
    return interval_value*(Y[first]+Y[last])/2

def simpson_One_Third(X,Y,first,last,interval_value):

    mid=math.floor((last+first)/2)
    
    return interval_value*(Y[first]+4*Y[mid]+Y[last])/3
    
def simpson_Two_Eight(X,Y,first,last,interval_value):
    
    mid=math.floor((last+first)/2)
    
    return 3*interval_value*(Y[first]+3*Y[mid]+3*Y[1+mid]+Y[last])/8
            
'''
*************************************************************
Numerical Integration for same Ineterval Points
Sove funtion according fit
*************************************************************
'''

'''
def myfunction():
    myfunction.counter += 1
myfunction.counter = 0

 myfunction()
 print(myfunction.counter)
'''

def same_numericalIntegration(X,Y,first,last,interval):
    
    ing_sum=0
    n=interval
    
    interval_value=(X[last]-X[first])/n
    #print(interval)
    #print(interval_value)
    #print("elements in interval",n)
  
    '''
    s4_count=math.floor(n/3)
    rem_n_S3=n-s4_count*3
    s3_count=math.floor(rem_n_S3/2)
    t_count=rem_n_S3%2
    '''

    
    
    if(n==1):
         s4_count=0
         s3_count=0
         t_count=1

    else:
        t_count=0
        
        if(n%3==0):
            s4_count=math.floor(n/3)
            s3_count=0
        elif(n%3==1):
            s4_count=math.floor(n/3)-1
            s3_count=2
        elif(n%3==2):
            s4_count=math.floor(n/3)
            s3_count=1
            
    
    
    for i in range(s4_count):
        
        last=first+3
        part_sum= simpson_Two_Eight(X,Y,first,last,interval_value)
        plt.fill_between( X[first:last+1], Y[first:last+1], color="skyblue", alpha=0.5)
        ing_sum=ing_sum+part_sum
        first=last
        #print(first,last,interval_value)
        
    for i in range(s3_count):
        
        last=first+2
        part_sum= simpson_One_Third(X,Y,first,last,interval_value)
        plt.fill_between( X[first:last+1], Y[first:last+1], color="yellow", alpha=0.5)
        ing_sum=ing_sum+part_sum
        first=last
        #print(first,last,interval_value)
    
    if(t_count==1):
        #print(trapezoidal(X,Y,first,last,interval_value))
        ing_sum=ing_sum+trapezoidal(X,Y,first,last,interval_value)
        plt.fill_between( X[first:last+1], Y[first:last+1], color="violet", alpha=0.5)
        #print(first,last,interval_value)
    #print("intervals",s4_count,s3_count,t_count)
    
    return ing_sum,s4_count,s3_count,t_count
    
            
'''
*************************************************************
Numerical Integration for any Ineterval and Points
Sove funtion 
*************************************************************
'''

def numerical_Integration(X,Y):
    
    firstIndex=0;
    interval=0;
    inerval_value=X[1]-X[0]
    
    numerical_intg_sum=0
    trap_inerval=0
    s3_inerval=0
    s4_inerval=0
    
    error_float_bit=.00001
    
    #print(X)
    #print(Y)
    
    for lastIndex in range(1,len(X)):
        
        new_inerval_value=X[lastIndex]-X[lastIndex-1]
        #print(new_inerval_value)
        
        
        if(abs(new_inerval_value-inerval_value)<error_float_bit):
            interval=interval+1
            
            if(lastIndex==len(X)-1):
            
                p_sum,s4p,s3p,tp=same_numericalIntegration(X,Y,firstIndex,lastIndex,interval)
            
                trap_inerval=trap_inerval+tp
                s3_inerval=s3_inerval+s3p
                s4_inerval=s4_inerval+s4p
                numerical_intg_sum=numerical_intg_sum+p_sum

                #print("Details",X[firstIndex],X[lastIndex],interval,new_inerval_value)            
            
        else :
            inerval_value=new_inerval_value
            
            p_sum,s4p,s3p,tp=same_numericalIntegration(X,Y,firstIndex,lastIndex-1,interval)
            
            trap_inerval=trap_inerval+tp
            s3_inerval=s3_inerval+s3p
            s4_inerval=s4_inerval+s4p
            numerical_intg_sum=numerical_intg_sum+p_sum

            #print("Details",X[firstIndex],X[lastIndex-1],interval,inerval_value)
            
            firstIndex=lastIndex-1
            interval=1
    
    if((len(X)-1)!=trap_inerval+s3_inerval*2+s4_inerval*3):
      
        p_sum,s4p,s3p,tp=same_numericalIntegration(X,Y,firstIndex,lastIndex,interval)
        
        trap_inerval=trap_inerval+tp
        s3_inerval=s3_inerval+s3p
        s4_inerval=s4_inerval+s4p
        numerical_intg_sum=numerical_intg_sum+p_sum
        
        
    return trap_inerval,s3_inerval,s4_inerval,numerical_intg_sum
            


'''
*************************************************************
Ploating Graph Point
Designing graph
*************************************************************
'''    
        
rnd = np.random.RandomState(0)        
colors = rnd.rand(len(X))


plt.figure(figsize=(12,8))
plt.xlabel(" X values ",weight='bold',size='x-large')
plt.ylabel(" Y values ",weight='bold',size='x-large')
plt.title(" ### Numerical Integration ### ",weight='bold',size='x-large')


plt.scatter(X, Y,c="black", s=60, alpha=1)


plt.plot(X,Y,label="Desire Curve",c="blue")

plt.grid()

last=len(X)-1
plt.fill_between( X[0:1], Y[0:1], color="skyblue", alpha=0.5,label="Simpson’s 3/8 rule")
plt.fill_between( X[0:1], Y[0:1], color="yellow", alpha=0.5,label="Simpson’s 1/3 rule")
plt.fill_between( X[last:last+1], Y[last:last+1], color="violet", alpha=0.5,label="Trapeziod 3/8 rule")

'''
*************************************************************
Numerical Integration for any Ineterval and Points
Main Code
*************************************************************
'''
        
t,s3,s4,ing=numerical_Integration(X,Y)

print("\nTrapezoidal rule: ",t," intervals")
print("1/3 rule ",s3*2," intervals")
print("3/8 rule: ",s4*3," intervals")
print("\nIntegral value: ",ing)

plt.legend()
plt.show()

'''
#ERROR TEST
n=10
s4_count=math.floor(n/3)
rem_n_S3=n-s4_count*3
s3_count=math.floor(rem_n_S3/2)
t_count=rem_n_S3%2
print(s4_count,s3_count,t_count)
'''
