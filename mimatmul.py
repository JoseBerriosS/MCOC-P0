#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:42:54 2020

@author: joseberrios
"""
import scipy as sp
def mimatmul(A,B):
    resultado = []
    for i in range(0,len(A)):
        lista=[]
        for j in range(0,len(B[0])):
            s = 0
            for k in range(0,len(A[0])):
                s += A[i][k]*B[k][j]
            lista.append(s)
        resultado.append(lista)
    
    return sp.matrix(resultado)
