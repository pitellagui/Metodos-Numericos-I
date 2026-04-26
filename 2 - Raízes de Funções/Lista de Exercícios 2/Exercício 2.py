"""
Exercício 2:

Use a bissecção e a falsa posição para localizar a raiz de f(x)=x^10-1
entre x=0 e x=1,3. Explique os resultados através da análise do erro
percentual estimado.
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# Definição da função e o intervalo
def func(x):
  return x**10 - 1

xmin = 0
xmax = 1.3

# Definição da função e o intervalo
def func(x):
  return x + np.log(x)

xmin = 0.2
xmax = 2

# Gráfico
x = np.linspace(xmin,xmax,100)
plt.plot(x,func(x),'-',color='blue',label='f(x)')
plt.plot(np.linspace(xmin,xmax,100),np.linspace(0,0,100),'--',color='black')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()

def bissec(func, xl, xu, Eppara, maxit, *args):

    if func(xl, *args) * func(xu, *args) > 0:
        raise ValueError('Não há mudança de sinal')

    iter = 0
    xr_new = xl
    nn = []
    estimativa = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:
        xr_old = xr_new
        xr_new = (xl + xu) / 2
        iter += 1

        if xr_new != 0:
           Epest = abs((xr_new - xr_old) / xr_new) * 100

        test = func(xl, *args) * func(xr_new, *args)

        if test < 0:
            xu = xr_new
        elif test > 0:
            xl = xr_new
        else:
            Epest = 0

        k = k + 1 # Contador

        # Salvando o número de iterações e as estimativas dos erros
        nn.append(k)
        estimativa.append(xr_new)
        E_pest.append(Epest)

    raiz = xr_new

    fx = func(xr_new, *args)

    # Data Frame
    table_biss = pd.DataFrame()
    table_biss['n'] = nn
    table_biss['Estimativa'] = estimativa
    table_biss['Epest (%)'] = E_pest

    return raiz, fx, Epest, iter, nn, estimativa, E_pest, table_biss

def falsa_posicao(func, xl, xu, Eppara, maxit, *args):

    if func(xl, *args) * func(xu, *args) > 0:
        raise ValueError('Não há mudança de sinal')

    iter = 0
    xr_new = xl
    nn = []
    estimativa = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:
        xr_old = xr_new
        xr_new = xu - (func(xu, *args)*(xl - xu))/(func(xl, *args) - func(xu, *args))
        iter += 1

        if xr_new != 0:
            Epest = abs((xr_new - xr_old) / xr_new) * 100

        test = func(xl, *args) * func(xr_new, *args)

        if test < 0:
            xu = xr_new
        elif test > 0:
            xl = xr_new
        else:
            Epest = 0

        k = k + 1 # Contador

        # Salvando o número de iterações e as estimativas dos erros
        nn.append(k)
        estimativa.append(xr_new)
        E_pest.append(Epest)

    raiz = xr_new

    fx = func(xr_new, *args)

    # Data Frame
    table_fp = pd.DataFrame()
    table_fp['n'] = nn
    table_fp['Estimativa'] = estimativa
    table_fp['Epest (%)'] = E_pest

    return raiz, fx, Epest, iter, nn, estimativa, E_pest, table_fp

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)
tam =1
# Número Máximo de Iterações
maxit = 100

print('----------------Método da Bissecção----------------')
for i in range(0,tam):
  # Intervalo
  xl = xmin
  xu = xmax
  [x, fx, Epest, iter, nn, estimativa, E_pest, table_biss] = bissec(func, xl, xu, Eppara, maxit)

print(table_biss)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()
print('---------------------------------------------------')
print()

print('--------------Método da Falsa Posição--------------')
for i in range(0,tam):
  # Intervalo
  xl = xmin
  xu = xmax
  [x, fx, Epest, iter, nn, estimativa, E_pest, table_fp] = falsa_posicao(func, xl, xu, Eppara, maxit)

print(table_fp)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()
print('---------------------------------------------------')