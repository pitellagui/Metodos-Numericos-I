"""
Exemplo 2:

Use o método da bissecção para resolver o problema do Bungee Jumping.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def bissec(func, xl, xu, Eppara, maxit, x_ex, *args):

    if func(xl, *args) * func(xu, *args) > 0:
        raise ValueError('Não há mudança de sinal')

    iter = 0
    xr_new = xl
    nn = []
    estimativa = []
    E_pt = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:
        xr_old = xr_new
        xr_new = (xl + xu) / 2
        iter += 1

        if xr_new != 0:
            Ept = abs((x_ex - xr_new) / x_ex) * 100
            print(Ept)
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
        E_pt.append(Ept)
        E_pest.append(Epest)

    raiz = xr_new

    fx = func(xr_new, *args)

    return raiz, fx, Epest, iter, nn, estimativa, E_pt, E_pest

# Exemplo de uso:
# Dados de Entrada
v = 36 # m/s
g = 9.81 # m/s
t = 4 # s
c_d = 0.25 # kg/m

# Intervalo
xl = 50
xu = 200

# Critério de Scarvorought, 1966
n = 3 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

# Solução Exata
x_ex = 142.7376

def func(m, v, g, t, c_d):
  return np.sqrt((g*m)/c_d)*np.tanh(np.sqrt((g*c_d)/m)*t)-v

[m, fx, Epest, iter, nn, estimativa, E_pt, E_pest] = bissec(func, xl, xu, Eppara, maxit, x_ex, v, g, t, c_d)


# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativa
table['Ept (%)'] = E_pt
table['Epest (%)'] = E_pest

print(table)
print()

print('raiz:', m)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()

# Gráficos
plt.plot(table['n'],table['Ept (%)'],'o--',color='blue',label='Ept (%)')
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()