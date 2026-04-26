"""
Exercício 2:

Dado:

    f(x) = -1,5x^6 - 2x^4 + 12x

a) Faça um gráfico da função.

b) Encontre o valor de x que maximiza a função f(x) utilizando a busca
da razão áurea. Empregue aproximações iniciais de xl = 0 e xu = 2.

c) Ache o valor de x que maximiza a função f(x) utilizando a interpolação
quadrática. Empregue aproximações iniciais de x1 = 0, x2 = 1 e x3 = 2.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def func(x):
    return -1.5*x**6-2*x**4+12*x

# Gráfico
x = np.linspace(0,1.5,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')

plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.xlim(0,1.5)
plt.ylim(-10,10)
plt.show()


def aureamin(func, xl, xu, Eppara, maxit, *args):
    phi = (1 + math.sqrt(5)) / 2
    iter = 0
    Ea = 100
    nn = []
    x_otimo = []
    func_otimo = []
    E_a = []

    while Ea >= Eppara and iter < maxit:
        d = (phi - 1) * (xu - xl)
        x1 = xl + d
        x2 = xu - d

        if func(x1, *args) < func(x2, *args):
            xopt = x1
            xl = x2
        else:
            xopt = x2
            xu = x1

        iter += 1
        if xopt != 0:
            Ea = (2 - phi) * abs((xu - xl) / xopt) * 100

        # Salvando o número de iterações e as estimativas dos erros
        nn.append(iter)
        x_otimo.append(xopt)
        func_otimo.append(func(xopt, *args))
        E_a.append(Ea)

    return xopt, func(xopt, *args), Ea, iter, nn, x_otimo, func_otimo, E_a

def func(x):
    return -(-1.5*x**6-2*x**4+12*x) # - pq transformamos o ponto máximo em mínimo

# Intervalo
xl = 0
xu = 2

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

# Busca da razão áurea
[xopt, fopt, Ea, iter, nn, x_otimo, func_otimo, E_a] = aureamin(func, xl, xu, Eppara, maxit)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['xopt'] = x_otimo
table['funcopt'] = func_otimo
table['Ea (%)'] = E_a

print(table)
print()


def iterpol_quad(func, x1, x2, x3, Eppara, maxit, *args):

    iter = 0
    Epest = 100
    nn = []
    x_4 = []
    func_x4 = []
    E_pest = []
    x4 = x2 - (1/2)*((x2 - x1)**2*(func(x2, *args) - func(x3, *args)) - (x2 - x3)**2*(func(x2, *args) - func(x1, *args)))/((x2 - x1)*(func(x2, *args) - func(x3, *args)) - (x2 - x3)*(func(x2, *args) - func(x1, *args)))
    x4_old = x4

    while Epest >= Eppara and iter < maxit:

        if func(x4_old, *args) < func(x2, *args):
            x1 = x2
            x2 = x4_old

        elif func(x4_old, *args) > func(x2, *args):
            x3 = x2
            x2 = x4_old

        x4_new = x2 - (1/2)*((x2 - x1)**2*(func(x2, *args) - func(x3, *args)) - (x2 - x3)**2*(func(x2, *args) - func(x1, *args)))/((x2 - x1)*(func(x2, *args) - func(x3, *args)) - (x2 - x3)*(func(x2, *args) - func(x1, *args)))
        iter += 1
        if x4 != 0:
            Epest = abs((x4_new - x4_old) / x4_new) * 100

        x4_old = x4_new
        # Salvando o número de iterações e as estimativas dos erros
        nn.append(iter)
        x_4.append(x4_new)
        func_x4.append(func(x4_new, *args))
        E_pest.append(Epest)

    return x4_new, func(x4, *args), Epest, iter, nn, x_4, func_x4, E_pest

def func(x):
    return -(-1.5*x**6-2*x**4+12*x) # - pq transformamos o ponto máximo em mínimo

# Aproximações
x1 = 0
x2 = 1
x3 = 2

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

# Interpolação quadrática
[x4, funcx4, Epest, iter, nn, x_4, func_x4, E_pest] = iterpol_quad(func, x1, x2, x3, Eppara, maxit)


# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['x4'] = x_4
table['func_x4'] = func_x4
table['Epest (%)'] = E_pest

print(table)
print()