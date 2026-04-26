"""
Exercício 5:

Use os métodos da falsa posição e da secante para fazer uma estimativa
da raiz de f(x)=ln(x). Comece os cálculos com os valores xl = x_(i-1) = 0,5
e xu = x_i = 5,0.
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

    # Data Frame
    table_s = pd.DataFrame()
    table_s['n'] = nn
    table_s['Estimativa'] = estimativa
    table_s['Epest (%)'] = E_pest

    return raiz, fx, Epest, iter, nn, estimativa, E_pest, table_s

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

# Chute Inicial para Secante e Falsa Posição
x_i_1 = 0.5
x_i = 5
xl = x_i_1
xu = x_i

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100

def func(x):
  return np.log(x)


# Método da Secante
print('-----------------Método da Secante------------------')
[x, fx, Epest, iter, nn, estimativa, E_pest, table_s] = secante(func, x_i_1, x_i, Eppara, maxit)

print(table_s)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()
print('---------------------------------------------------')
print()

# Método da Falsa Posição
print('--------------Método da Falsa Posição--------------')
[x, fx, Epest, iter, nn, estimativa, E_pest, table_fp] = falsa_posicao(func, xl, xu, Eppara, maxit)

print(table_fp)
print()

print('raiz:', x)
print('Epest:', Epest)
print('Número de iterações:', iter)
print()
print('---------------------------------------------------')
print()



# Gráficos
plt.plot(table_s['n'],table_s['Epest (%)'],'o--',color='red',label='Método da Secante')
plt.plot(table_fp['n'],table_fp['Epest (%)'],'o--',color='blue',label='Método da Falsa Posição')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Estimado (%)')
plt.legend()
plt.show()