#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:56:53 2020

@author: joseberrios
"""

import scipy as sp
from time import perf_counter


nombre = ('jose')

print (3*f'Hola MCOC {nombre} ')

N = 1000

A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))

t1 = perf_counter()
C = A*B
t2 = perf_counter()

dt = t2 - t1


print(f'\nMatriz C de {N}x{N}\n')

print(f'Tiempo transcurrido = {dt} s')
