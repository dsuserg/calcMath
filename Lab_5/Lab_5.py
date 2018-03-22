#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:37:34 2017
`
@author: sergey
"""
import Fibonachi as fib

fib.Start()
E=0.001

a0 = -0.19
a1 = 0.63
a2 = -4.28
a3 = 1.15

X_left = -4.5
X_right =  -3.5
Min=-4
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

X_left = 1.0
X_right =  2.0
Min=1.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

X_left = 6.0
X_right =  7.0
Min=6.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

E=0.1
X_left = -10.0
X_right =  -9.0
Min=-9.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

E=0.01
X_left = -10.0
X_right =  -9.0
Min=-9.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

E=0.001
X_left = -10.0
X_right =  -9.0
Min=-9.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)

E=0.0001
X_left = -10.0
X_right =  -9.0
Min=-9.5
fib.Fibonachi_Method(X_left,X_right,E,a0,a1,a2,a3,Min)