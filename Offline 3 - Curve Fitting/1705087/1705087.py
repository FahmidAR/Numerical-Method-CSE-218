# -*- coding: utf-8 -*-

"""
*************************************************************
Created on Thu Jul 25 12:15:26 2019
@author: Fahmid_1705087
*************************************************************
"""

import numpy as np
from matplotlib import pyplot as plt

"""
*************************************************************
LU Deco
Solving Matrics
*************************************************************
"""

def luFuntionFahmid(n,A):
    
    L=np.zeros((n,n))
    U=A
    flagIsSolve=True
    
    for i in range(0, n):
        
        L[i,i]=1
        
    for i in range(0, n-1):
        
        for j in range(i+1, n):
            
            x=U[j,i]/U[i,i]
            L[j,i]=x
            
            U[j,:]=A[i,:]*(-x)+U[j,:]
    
    
    
    for i in range(0, n):
        for j in range(0, n):
            
            max=0
            if(U[i,j]!=0):
                max=1
        if(max==0):
            flagIsSolve=False
            break
    
    return L,U,flagIsSolve

def yCalcuFahmid(n,L,B):
    
    Y=np.zeros((n,1))
    
    Y[0,0]=B[0,0]
    
    for i in range(1,n):
        
        sum=0
        
        for j in range(0,i):
            
            sum+=Y[j,0]*L[i,j]
        
            Y[i,0]=(B[i,0]-sum)
    
    return Y
    
    
def xCalcuFahmid(n,Y,U):
    
    X=np.zeros((n,1))
    
    X[n-1,0]=(Y[n-1,0])/U[n-1,n-1];
    
    for i in range(n-2,-1,-1):
        sum=0
        
        for j in range(n-1,i,-1):
            
            sum+=U[i,j]*X[j,0]
            
            X[i,0]=(Y[i,0]-sum)/U[i,i];

    return X

'''
*************************************************************
Input taking from file 
Makig list with points
*************************************************************
'''
listAllNumber=[]
X=[]
Y=[]

flag=1

with open("data.txt", "r+") as f:
    lines=f.readlines()
    for line in lines:
        listAllNumber+=line.strip().split(" ")

#print(listAllNumber)

for num in listAllNumber:
    
    if(flag==1):
        X.append(float(num))
        flag=0
    else:
        Y.append(float(num))
        flag=1

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
Array of Polynmiyal Regression Making 
Sove funtion 
*************************************************************
'''

def sumGenarateofPowerOfX(X,n):
    sum=0
    for x in X:
        sum+=x**n
    return sum

def sumGenarateofPowerOfXY(X,Y,n):
    sum=0
    for i in range(0,len(X)):
        sum+=Y[i]*(X[i]**n)
    return sum


def regArrayMakingFromPoint(X,Y,order):
     order=order+1
     A=np.zeros((order,order))
     
     xList=[]
     xList.append(len(X))
     for i in range(1,order+order-1):
         xList.append(sumGenarateofPowerOfX(X,i))
     
     for c in range(0,order):
         for r in range(0,order):
             A[r,c]=xList[r+c]
     
     B=np.zeros((order,1))
     
     for r in range(0,order):
         B[r,0]=sumGenarateofPowerOfXY(X,Y,r)
    
     return A,B  
     


'''
*************************************************************
Ploating Graph Point
Designing graph
*************************************************************
'''    
        
rnd = np.random.RandomState(0)        
colors = rnd.rand(len(X))
sizes = 20 * rnd.rand(len(X))

plt.figure(figsize=(13,10))
plt.xlabel(" X values ",weight='bold',size='x-large')
plt.ylabel(" Y values ",weight='bold',size='x-large')
plt.title(" ### Curve Fitting ### ",weight='bold',size='x-large')


plt.scatter(X, Y,c=colors, s=sizes, alpha=0.7)


'''
*************************************************************
Calculation Regressioon 
Sove funtion 
*************************************************************
'''
def correctionC(Y,Z):
    
    sum=0
    
    data = np.array(Y,dtype=np.float32)
    row=len(data)
    
    for i in range(row):
        sum=sum+data[i]
        
    yBar=sum/len(Y)
    
    sT=0
    for elememt in Y:
        sT+=(elememt-yBar)**2
    
    sR=0
    for i in range(len(Y)):
        sR+=(Y[i]-Z[i])**2
    
    r2=(sT-sR)/sT
    
    return r2**(1/2)

'''
*************************************************************
Multiple Linear Regressioon 
Sove funtion 
*************************************************************
'''

def oneYfromlinearFuntion(a,x):
    sum=0
    power=0
        
    for element in a:
        sum+=element*(x**power)
        power+=1
    #print(sum[0])
    return sum[0]

def AllYfromlinearFuntion(a,X):
    Y=[]
    for element in X:
         Y.append(oneYfromlinearFuntion(a,element))
         
    return Y

def printArray(a):
    
    for i in range(0,len(a)):
        print("a",i," = ",a[i])
    print("\n")

'''
*************************************************************
Multiple Linear Regressioon 
Sove funtion 
Ploating Graph Poly Equ
*************************************************************
'''

for num in range(1,4):
    
    
    order=num
    n=order+1
    
    A,B=regArrayMakingFromPoint(X,Y,order)
    L,U,flag=luFuntionFahmid(n,A)
    b=yCalcuFahmid(n,L,B)
    a=xCalcuFahmid(n,b,U)
    
    
    Z=AllYfromlinearFuntion(a,X)
    
    print("\n### Value of An serailly linear equ of",num,"order\n")
    printArray(a)
    
    cc=correctionC(Y,Z)
    print("Correction Co-efficient  = ",cc)
    
    #print(a)
    #print(X)
    #print(Y)
    #print(Z)
    
    #plt.plot(X,Y)
    s=" Order of "+str (num)
    plt.plot(X,Z,label=s)
    plt.legend(loc='lower right')
    plt.grid()
    
plt.show()   
         
'''
*************************************************************
THE END happy coding 1705087
*************************************************************
''' 