"""
Exercício 1:

Use a busca da razão áurea para resolver o Exemplo 1.

Exemplo 1:

Determine o tempo e o valor da elevação máxima com base na equação:

    z = z0 + (m/c)(v0 + mg/c)(1 - e^(-(c/m)t)) - (mg/c)t

Use os seguintes parâmetros em seus cálculos:

    g = 9,81 m/s^2
    z0 = 100 m
    v0 = 55 m/s
    m = 80 kg
    c = 15 kg/s
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

# Dados Iniciais
g = 9.81 # m/s^2
z_0 = 100 # m
v_0 = 55 # m/s
m = 80 # kg
c = 15 # kg/s

# Intervalo
xl = 0
xu = 8

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 100

def func(t, g, z_0, v_0, m, c):
    return -(z_0 + m/c*(v_0 + m*g/c)*(1 - np.exp(-(c/m)*t))- (m*g/c)*t)

# Busca da razão áurea
[xopt, fopt, Ea, iter, nn, x_otimo, func_otimo, E_a] = aureamin(func, xl, xu, Eppara, maxit, g, z_0, v_0, m, c)


# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['xopt'] = x_otimo
table['funcopt'] = func_otimo
table['Ea (%)'] = E_a

print(table)
print()


# Gráfico
t = np.linspace(xl,xu,100)
plt.plot(t,-func(t, g, z_0, v_0, m, c),'-',color='blue',label='fx)')
plt.plot(xopt,-fopt,'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(t)')
plt.xlabel('t')
plt.grid()
plt.show()

import math

def quad_interp_min(func, x1, x2, x3, es=1e-6, maxit=100):
    iter = 0
    ea = float('inf')

    while ea > es and iter < maxit:
        # Avaliar a função nos três pontos
        f1, f2, f3 = func(x1), func(x2), func(x3)

        # Ajustar uma parábola aos três pontos
        a0 = f1
        a1 = (f2 - f1) / (x2 - x1)
        a2 = ((f3 - f1) / (x3 - x1) - a1) / (x3 - x2)

        # Encontrar o mínimo da parábola ajustada
        xopt = 0.5 * (x1 + x2 - a1 / a2)

        # Ajustar os intervalos
        x1, x2, x3 = sorted([x1, x2, x3] + [xopt])

        # Calcular o erro aproximado
        ea = abs((xopt - x2) / xopt) * 100

        iter += 1

    return xopt, func(xopt), ea, iter

# Exemplo de uso:
def example_function(x):
    return x**2 / 10 - 2 * math.sin(x)

x1, x2, x3 = 0, 2, 4

result = quad_interp_min(example_function, x1, x2, x3)
print(result)
print()