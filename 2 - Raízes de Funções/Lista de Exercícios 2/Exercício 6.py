"""
Exercício 6:

Use o método da secante modificada para fazer uma estimativa da raiz da
f(x)=e^(-x)-x. Use um valor de 0,01 para delta e comece com x0=1,0.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def secante_modificado(func, x_0, delta, Eppara, maxit, *args):

    iter = 0
    x_old = x_0
    nn = []
    estimativa = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:

        x_new = x_old - delta*x_old*func(x_old, *args)/(func(x_old + delta*x_old, *args) - func(x_old, *args))
        iter += 1

        if x_new != 0:
            Epest = abs((x_new - x_old) / x_new) * 100

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
x_0 = 1

# Fração de perturbação
delta = 0.01

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

def func(x):
  return np.exp(-x) - x

[x, fx, Epest, iter, nn, estimativa, E_pest] = secante_modificado(func, x_0, delta, Eppara, maxit)


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