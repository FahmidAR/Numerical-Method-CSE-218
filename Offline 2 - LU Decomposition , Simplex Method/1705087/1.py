# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:15:25 2019

@author: FAHMID 1705087
"""

import numpy as np

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

inputFile=open('in1.txt','r')

n=int(inputFile.readline())

A=np.fromfile(inputFile,count=n*n, sep= " ")
A=np.reshape(A,(n,n))

B=np.fromfile(inputFile,count=n, sep= " ")
B=np.reshape(B,(n,1))

inputFile.close()

'''
A = np.array([[1,1,1],[4,3,-1],[3,5,3]])

B = np.array([[1],[6],[4]])
'''

L ,U,flag=luFuntionFahmid(n,A)
Y=yCalcuFahmid(n,L,B)
X=xCalcuFahmid(n,Y,U)

outputFile=open('out1.txt','w')

    
np.savetxt(outputFile,L, fmt='%.4f')
outputFile.write("\n")
np.savetxt(outputFile, U, fmt='%.4f')
outputFile.write("\n")

if(flag):
    for element in Y:
        np.savetxt(outputFile,element, fmt='%.4f')
    outputFile.write("\n")
    for element in X:
        np.savetxt(outputFile,element, fmt='%.4f')
else:
    outputFile.write("No unique solution")


outputFile.close()    
         
    
    
    