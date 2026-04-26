"""
Exercício 3:

A equação de Ergun

    (ΔPρ / G0^2)(Dp / L)(ε / (1 - ε)) =
    150((1 - ε) / (DpG0 / μ)) + 1,75

é usada para descrever o escoamento de um fluido através de um leito
compactado.

Dados:

    DpG0 / μ = 1000

    ΔPρDp / (G0^2L) = 20

Encontre a fração vazia ε do leito.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def func(x):
  C1 = 1000 # \frac{D_p G_0}{\mu}
  C2 = 20 # \frac{\Delta P \rho D_p}{G_0^2 L}
  return C2*(x/(1-x)) - 150*(1-x)/(C1) - 1.75

# Gráfico
xmin = 0
xmax = 0.1
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

# Critério de Scarvorought, 1966
n = 12 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

print('----------------Método da Bissecção----------------')
xl = xmin
xu = xmax
[x, fx, Epest, iter, nn, estimativa, E_pest, table_biss] = bissec(func, xl, xu, Eppara, maxit)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativa
table['Epest (%)'] = E_pest

print(table)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()

# Gráficos
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()