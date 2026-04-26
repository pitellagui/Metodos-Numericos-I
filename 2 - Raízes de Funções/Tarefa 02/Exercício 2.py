"""
Exercício 2:

Localize a primeira raiz positiva de:

    f(x) = sin(x) + cos(1 + x^2) - 1

onde x está em radianos. Use o método da secante para um valor de Epest
correspondente a seis algarismos significativos com as seguintes aproximações
iniciais:

a) x_(i-1) = 1,0 e x_i = 3,0
b) x_(i-1) = 1,5 e x_i = 2,5
c) x_(i-1) = 1,5 e x_i = 2,25

para localizar a raiz.

d) Use o método gráfico para explicar seus resultados.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def func(x):

  return np.sin(x) + np.cos(1 + x**2) -1

# Gráfico
xmin = -300
xmax = np.pi
x = np.linspace(xmin,xmax,100)
plt.plot(x,func(x),'-',color='blue',label='f(x)')
plt.plot(np.linspace(xmin,xmax,100),np.linspace(0,0,100),'--',color='black')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()

def secante(func, x_i_1, x_i, Eppara, maxit, *args):

    iter = 0
    x_old_old = x_i_1
    x_old = x_i
    nn = []
    estimativa = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:

        x_new = x_old - func(x_old, *args)*(x_old - x_old_old)/(func(x_old, *args) - func(x_old_old, *args))
        iter += 1

        if x_new != 0:
            Epest = abs((x_new - x_old) / x_new) * 100

        x_old_old = x_old
        x_old = x_new
        k = k + 1 # Contador

        # Salvando o número de iterações e as estimativas dos erros
        nn.append(k)
        estimativa.append(x_new)
        E_pest.append(Epest)

    raiz = x_new

    fx = func(x_new, *args)

    # Data Frame
    table_s = pd.DataFrame()
    table_s['n'] = nn
    table_s['Estimativa'] = estimativa
    table_s['Epest (%)'] = E_pest

    return raiz, fx, Epest, iter, nn, estimativa, E_pest, table_s

# Chute Inicial para Secante e Falsa Posição
x_i_1 = 1.5
x_i = 2.25

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

# Método da Secante
print('-----------------Método da Secante------------------')
[x, fx, Epest, iter, nn, estimativa, E_pest, table] = secante(func, x_i_1, x_i, Eppara, maxit)

print(table)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()
print('---------------------------------------------------')
print()




# Gráficos
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()