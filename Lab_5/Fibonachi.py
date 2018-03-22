#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:37:34 2017
`
@author: sergey
"""
import math

def Start(): 
    Starts=open('Variant','r')
    for line in Starts:
        print(line)
    print("-----------------------------------------------------------------------------------------")
        
def Myfunc(x,a0,a1,a2,a3):
    solve=a0+a1*x+a2*math.sin(a3*x)
    return solve
    
def Fibonachi_gen(N):
    F=[1,1]
    
    i=1
    
    while True:
        F.append(F[i]+F[i-1])
        i+=1
        if F[i] >= N:
            break
    return F

def Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min):
    N=(X_right-X_left)/E
    F=[]
    F=Fibonachi_gen(N)
    k=len(F)-1
    
    dx=(X_right-X_left)/F[k]
    
    i=1
    
    x1=X_left+dx*F[k-i-1]
    x2=X_left+dx*F[k-i]
    R1=Myfunc(x1,a0,a1,a2,a3)
    R2=Myfunc(x2,a0,a1,a2,a3)
    print("Метод Чисел фибоначи, E= " + str(E) + ", Шаг= " + str(dx) + ", x= " + str(Min))
    print(' {0:2} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10}'.format("i","X_left","x1","x2","X_right","R1","R2"))        
    print('{0:2d} {1:10f} {2:10f} {3:10f} {4:10f} {5:10f} {6:10f}'.format(i,X_left,x1,x2,X_right,R1,R2))
    
    i=2
    while i<=k:
        if R1<R2:
            X_right=x2
            x2=x1
            x1=X_left+dx*F[k-i]
        elif R2<R1:
            X_left=x1    
            x1=x2
            x2=X_left+dx*F[k-i-1]
        elif R1==R2:
            x1=X_left+dx*F[k-i]
            x2=X_left+dx*F[k-i-1]  
        R1=Myfunc(x1,a0,a1,a2,a3)
        R2=Myfunc(x2,a0,a1,a2,a3)    
        print('{0:2d} {1:10f} {2:10f} {3:10f} {4:10f} {5:10f} {6:10f}'.format(i,X_left,x1,x2,X_right,R1,R2))
        i+=1 
    print("-----------------------------------------------------------------------------------------")        
        