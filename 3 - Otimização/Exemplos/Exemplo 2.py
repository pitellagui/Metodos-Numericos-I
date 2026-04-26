"""
Exemplo 2:

Use a busca da razão áurea para achar o mínimo de:

    f(x) = x^2/10 - 2sin(x)

no intervalo entre xl = 0 e xu = 4.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

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

# Intervalo
xl = 0
xu = 4

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

def func(x):
    return (x**2) / 10 - 2 * np.sin(x)

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


# Gráfico
x = np.linspace(xl,xu,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')
plt.plot(xopt,fopt,'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()