#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:32:03 2020

@author: joseberrios
"""
import scipy as sp
from scipy import linalg
import numpy as np
from numpy import zeros, float16, float32, float64, float128
from time import perf_counter
import matplotlib.pyplot as plt


def Laplace(N, dtype=float128):
    A = zeros((N,N), dtype=float128)
    for i in range(N):
        A[i,i] = 2
        for j in range(N):
            if i+1 == j or i-1 == j:
                A[i,j] = -1             
    return (A)



Ns = [2, 5, 10, 12, 20, 35, 40, 45, 50 , 55, 60, 75, 100, 125, 160, 200,
      350, 500, 1000, 2000, 5000]


Ncorridas = 5

for i in range (Ncorridas):
    dts = []
    mem= []
    name= (f'inversa{i}.txt')
    fid = open (name, 'w')
    
    for N in Ns:
        
        A = Laplace(N)
        
        t1 = perf_counter()
        
        C = np.linalg.inv(A)
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        size = 3*(N**2)*16
        
        dts.append(dt)
        mem.append(size)
        
        fid.write(f'{N} {dt} {size}\n')
        
        fid.flush()
        
    fid.close()
    
            
plt.figure()
for i in range(Ncorridas):
        
        archivo = open(f"inversa{i}.txt", "r")
    
        lineas = []
        x =[]
        y_t =[]
        y_m = []
        
        for linea in archivo.readlines():
            a=linea.strip('\n')
            b = a.split(' ')
            c = [float(i) for i in b]
            lineas.append(c)
            
            
        for i in lineas:
            x.append(int(i[0]))
            y_t.append((i[1]))
            y_m.append(int(i[2]))
            
        
        plt.subplot(2, 1, 1)
        
        plt.grid(True)
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(x, y_t, '-o')
        plt.title('Rendimiento funcion inversa')
        plt.ylabel('Tiempo Transcurrido')
        plt.xticks((10,20,50,100,200,500,1000,2000,5000,10000,20000), (''
                   , '', '', '', '', '', '',
                   '', '', '', ''))
        plt.yticks((0.0001,0.001,0.01,0.1,1,10,60,600), ('0.1 ms'
                   , '1 ms', '10 ms', '0.1 s', '1 s', '10 s', '1 m',
                   '10 m'))
        plt.xlim(0, 20000)  
        
        plt.subplot(2, 1, 2)
       
        plt.grid(True)
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(x, y_m, '-oc')
        plt.plot([0,20000],[16000000000,16000000000],'--')
        plt.xticks((10,20,50,100,200,500,1000,2000,5000,10000,20000), ('10'
                   , '20', '50', '100', '200', '500', '1000',
                   '2000', '5000', '10000', '20000'), rotation=30)
        plt.yticks((1000,10000,100000,1000000,10000000,100000000,
                    1000000000,10000000000), ('1 KB'
                   , '10 KB', '100 KB', '1 MB', '10 MB', '100 MB', '1 GB',
                   '10 GB'))
        plt.xlim(0, 20000)                                     
        
        plt.ylabel('Uso Memoria') 
        plt.xlabel('Tamaño de la Matriz')

plt.show()
