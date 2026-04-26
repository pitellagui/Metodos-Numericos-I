"""
Exemplo 5:

Use o método Brent para resolver o problema do Bungee Jumping e faça
uma análise do erro. Utilise como estimativas iniciais x_(i-1) = 50 e x_i = 200.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def fzerosimp(func, xl, xu, Eppara, *args):
    a = xl
    b = xu
    fa = func(a, *args)
    fb = func(b, *args)
    c = a
    fc = fa
    d = b - c
    e = d
    iterations = 0  # Contador de iterações

    while True:
        iterations += 1  # Incrementa o contador de iterações

        if fb == 0 or iterations >= maxit:
            break

        if np.sign(func(a, *args)) == np.sign(func(b, *args)):
            a = c
            fa = fc
            d = b - c
            e = d

        if np.abs(func(a, *args)) < np.abs(func(b, *args)):
            c = b
            b = a
            a = c
            fc = fb
            fb = fa
            fa = fc

        m = 0.5 * (a - b)
        tol = 2 * Eppara * np.max([np.abs(b - a), 1])

        if np.abs(m) <= tol or fb == 0:
            break

        if np.abs(e) >= tol and np.abs(fc) > np.abs(fb):
            s = fb / fc
            if a == c:
                p = 2 * m * s
                q = 1 - s
            else:
                q = fc / fa
                r = fb / fa
                p = s * (2 * m * q * (q - r) - (b - c) * (r - 1))
                q = (q - 1) * (r - 1) * (s - 1)

            if p > 0:
                q = -q
            else:
                p = -p

            if 2 * p < 3 * m * q - np.abs(tol * q) and p < np.abs(0.5 * e * q):
                e = d
                d = p / q
            else:
                d = m
                e = m
        else:
            d = m
            e = m

        c = b
        fc = fb
        if np.abs(d) > tol:
            b = b + d
        else:
            b = b - np.sign(b - a) * tol

        fb = func(b, *args)
        error = np.abs(fb)

    return b, iterations, error

# Dados de Entrada
v = 36  # m/s
g = 9.81  # m/s^2
t = 4  # s
c_d = 0.25  # kg/m

# Intervalo
xl = 50
xu = 200

# Critério de Scarvorought, 1966
n = 3  # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

# Solução Exata
x_ex = 142.7376

def func(m, v, g, t, c_d):
    return np.sqrt((g * m) / c_d) * np.tanh(np.sqrt((g * c_d) / m) * t) - v

# Chamada da função
m, num_iterations, error = fzerosimp(func, xl, xu, Eppara, v, g, t, c_d)

print('Raiz:', m)
print('Número de iterações:', num_iterations)
print('Erro na raiz:', error)