"""
Exemplo 3:

Use a interpolação quadrática para aproximar o ponto de mínimo de:

    f(x) = x^2/10 - 2sin(x)

com aproximações iniciais x_l = 0, x_2 = 1 e x_3 = 4.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

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



# Aproximações
x1 = 0
x2 = 1
x3 = 4

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

args = []
def func(x):
    return (x**2) / 10 - 2 * np.sin(x)

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



# Gráfico
x = np.linspace(x1,x3,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')
plt.plot(x4,funcx4,'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()