"""
Exercício 9: Refaça o Exemplo 4 e os Exercícios 6, 7 e 8 usando a iterpolação de Lagrange e compare os resultados com a interpolação de Newton.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import statistics as sts

def Lagranint(x, y, x_interp):

    n = len(x)
    interpolated_value = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        interpolated_value += term

    return interpolated_value

# Dados de entrada
x=np.array([1, 4, 5, 6])
y = np.log(x)


x_estimativa = 2

y_estimativa = Lagranint(x,y,x_estimativa)

print(y_estimativa)
print()

# Gráfico
xspan = np.linspace(min(x),max(x),100)
yspan = np.log(xspan)
plt.plot(xspan,yspan,'-',color='red')
plt.plot(x,y,'o',color='red')
plt.plot(x_estimativa,y_estimativa,'o',color='blue', label='Estimativa')
plt.ylabel('$f(x)$')
plt.xlabel('x')
plt.legend()
plt.grid(True)
plt.show()