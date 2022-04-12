# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:16:32 2019

@author: FAHMID 1705087
"""

import numpy as np

def basicOrNonbasic(A,p,r):
    
    flagIsValue=False
    index=-1
    countZero=0
    
    for i in range(0,r):
        
        if(A[i,p]==0):
            countZero=countZero+1
        else:
            index=i
            
    if(countZero==r-1):
        flagIsValue=True
    
    
    
    return flagIsValue,index

def simplexFahmid(A,c):
    
    m=len(A)
    n=len(A[0])    
    
    while True:
        
        negElement=0
        negColInd=-1
        
        for i in range(0,n):
            
            if(A[0,i]<negElement):
            
                negColInd=i
                negElement=A[0,i]
                
        if(negColInd==-1 or negElement>=0):
            break
        
        intercept= np.zeros((m))
        
        for i in range(1,m):
            intercept[i]=A[i,n-1]/A[i,negColInd]       
        
        minRowIndx=-1
        valuetemp=999999
        
        for i in range(1,m):
            if(intercept[i]<valuetemp):
                valuetemp=intercept[i]
                minRowIndx=i
        
        A[minRowIndx,:]=A[minRowIndx,:]/A[minRowIndx,negColInd]
        
        print(A)
        for i in range(0,m):
            if(minRowIndx!=i):
                A[i,:]=A[i,:]-A[i,negColInd]*A[minRowIndx,:]
            np.set_printoptions(suppress=True,precision=2)
            print(A)
            print("\n")
            
    print("maximum is =",A[0,n-1])
    
    for i in range(1,c):
        flag,ind=basicOrNonbasic(A,i,m)
        if(flag):
            print(" X",i," is =",A[ind,n-1])
        else:
            print(" X",i," is = 0")
            
    for i in range(c,n-1):
        flag,ind=basicOrNonbasic(A,i,m)
        if(flag):
            print(" S",i-c," is =",A[ind,n-1])
        else:
            print(" S",i-c," is = 0")
            
           


def inputMatrixDesire(A):
    
    r=len(A)
    c=len(A[0])
    cNew=r+c;
    B=np.zeros((r,cNew))
    
    B[0,0]=1
    
    A[0,:]=A[0,:]*(-1)
    
    for i in range(0,r):
        for j in range(0,c-1):
            B[i,j+1]=A[i,j]
    
    t=c
    
    for i in range(1,r):
        
        B[i,t]=1
        t=t+1
        
    for i in range(0,r):
            B[i,cNew-1]=A[i,c-1]
    
       
    return B
    
        
        
'''      
A = np.array([[1,-12,-10,0,0,0,0,0],[0,5,4,1,0,0,0,1700],[0,1,1,0,1,0,0,7],[0,4.5,3.5,0,0,1,0,1600],[0,1,2,0,0,0,1,500]])

B=np.array([[12,10,0],[5,4,1700],[1,1,7],[4.5,3.5,1600],[1,2,500]])

'''

file=open("in2.txt","r")

li1=[]
str1=file.readline()
str1 += '0'
li1.append(str1.split())

Z=np.array(li1,dtype=np.float32)

Y=np.loadtxt(file)

file.close()

row=len(Y)+1
col=len(Y[0])

B= np.zeros((row,col))

for j in range(0,col):
    B[0,j]=Z[0,j]

for i in range(0,row-1):
    for j in range(0,col):
        B[i+1,j]=Y[i,j]

A=inputMatrixDesire(B)

print(A)
print("\n")

simplexFahmid(A,col)