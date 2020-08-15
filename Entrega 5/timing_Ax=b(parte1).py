#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:35:11 2020

@author: joseberrios
"""
import scipy as sp
import numpy as np
from numpy import zeros
from time import perf_counter
import matplotlib.pyplot as plt


def Laplace(N):
    A = zeros((N,N))
    for i in range(N):
        A[i,i] = 2
        for j in range(N):
            if i+1 == j or i-1 == j:
                A[i,j] = -1             
    return (A)



Ns = [2, 5, 10, 12, 20, 35, 40, 45, 50 , 55, 60, 75, 100, 125, 160, 200,
      350, 500, 1000, 2000, 5000, 10000, 20000]


Ncorridas = 10

matrices = ['A_invB.txt', 'A_invB_npSolve.txt']

archivos = [open(matriz, 'w') for matriz in matrices]
    
for N in Ns:
    
    dts = np.zeros((Ncorridas, len(archivos)))
    
    for i in range(Ncorridas):
        
       
        
        A = Laplace(N)
        B = np.ones(N)
    
        t1 = perf_counter()
        
        #inviertiendo y multiplicando
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][0] = dt

        t1 = perf_counter()
        
        #utilizando np.Solve
        x = np.linalg.solve(A, B)
        
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][1] = dt
 
    dts_prom = [ np.mean(dts[:][j]) for j in range(len(archivos)) ]
    
    for j in range(len(archivos)):
        archivos[j].write(f'{N} {dts_prom[j]}\n')
        archivos[j].flush()

[archivo.close() for archivo in archivos]

       
plt.figure()

archivo= [open(matriz, 'r') for matriz in matrices]

#ploteo
cont=0
for matriz in archivo:
    lineas = []
    x = []
    y_t = []
    
    for linea in matriz.readlines():
        a=linea.strip('\n')
        b = a.split(' ')
        c = [float(i) for i in b]
        lineas.append(c)
        
        
    for i in lineas:
        x.append(int(i[0]))
        y_t.append((i[1]))

    cont=+1
    
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(x, y_t, '-o', label= matrices[cont])
    plt.ylabel('Tiempo Transcurrido')
    
    plt.xticks((10,20,50,100,200,500,1000,2000,5000,10000,20000), ('10'
                   , '20', '50', '100', '200', '500', '1000',
                   '2000', '5000', '10000', '20000'), rotation=45)
    plt.yticks((0.0001,0.001,0.01,0.1,1,10,60,600), ('0.1 ms'
               , '1 ms', '10 ms', '0.1 s', '1 s', '10 s', '1 m',
               '10 m'))
    plt.xlim(0, 20000)
    
    
    plt.xlabel('Tamaño de la Matriz')


plt.legend()
plt.show()
