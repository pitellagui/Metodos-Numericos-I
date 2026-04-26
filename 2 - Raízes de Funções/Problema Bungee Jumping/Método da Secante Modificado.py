"""
Exemplo 6:

Use o método da secante modificado para resolver o problema do Bungee Jumping
e faça uma análise do erro. Utilise como estimativa inicial x0 = 50 e
delta = 10^(-6) para a fração de perturbação.
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

# Exemplo de uso:
# Dados de Entrada
v = 36 # m/s
g = 9.81 # m/s
t = 4 # s
c_d = 0.25 # kg/m

# Chute Inicial
x_0 = 50

# Fração de perturbação
delta = 1e-6

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

def func(m, v, g, t, c_d):
  return np.sqrt((g*m)/c_d)*np.tanh(np.sqrt((g*c_d)/m)*t)-v

[m, fx, Epest, iter, nn, estimativa, E_pest] = secante_modificado(func, x_0, delta, Eppara, maxit, v, g, t, c_d)


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
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()