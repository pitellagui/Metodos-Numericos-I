"""
Exercício 4:

Use o método da secante para fazer uma estimativa da raiz da f(x)=e^(-x)-x.
Utilise como estimativas iniciais x_(-1) = 0 e x_0 = 1.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

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

    return raiz, fx, Epest, iter, nn, estimativa, E_pest

# Chute Inicial
x_i_1 = 0
x_i = 1

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

def func(x):
  return np.exp(-x) - x

[m, fx, Epest, iter, nn, estimativa, E_pest] = secante(func, x_i_1, x_i, Eppara, maxit)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativa
table['Epest (%)'] = E_pest

print(table)
print()

print('raiz:', m)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()

# Gráficos
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Estimado (%)')
plt.legend()
plt.show()