"""
Exercício 1:

Dada a fórmula:

    f(x) = -x^2 + 8x - 12

a) Determine o máximo e o valor correspondente de x para essa função
analiticamente, isto é, utilizando derivação.

SOLUÇÃO:

Seja:

    f(x) = -x^2 + 8x - 12

Calculando a derivada primeira:

    f'(x) = -2x + 8

Tomando:

    f'(x) = 0

Logo:

    -2x + 8 = 0

Ou seja:

    x = 4

é um ótimo local.

Substituindo x = 4 em f(x), obtemos o valor da função no ótimo local:

    f(x) = -4^2 + 8*4 - 12
    f(x) = -16 + 32 - 12
    f(x) = 4

Calculando a derivada segunda:

    f''(x) = -2

Como:

    f''(x) < 0

logo é um ponto de máximo.

b) Verifique se a equação de interpolação quadrática produz os mesmos
resultados com base nas aproximações iniciais:

    x1 = 0
    x2 = 2
    x3 = 6
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Aproximações
x1 = 0
x2 = 2
x3 = 6

def func(x):
    return -x**2+8*x-12

# Interpolação Quadrática
x4 = x2 - (1/2)*((x2 - x1)**2*(func(x2) - func(x3)) - (x2 - x3)**2*(func(x2) - func(x1)))/((x2 - x1)*(func(x2) - func(x3)) - (x2 - x3)*(func(x2) - func(x1)))

print(x4)
print()

# Gráfico
x = np.linspace(x1,x3,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')
plt.plot(x4,func(x4),'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()