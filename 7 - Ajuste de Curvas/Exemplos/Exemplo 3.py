"""
Exemplo 3:

Considere que se queira determinar os coeficientes da parábola:

    f(x) = a1 + a2x + a3x^2

que passa através dos três últimos valores de densidade da tabela apresentada
anteriormente:

    x1 = 300    f(x1) = 0,616

    x2 = 400    f(x2) = 0,525

    x3 = 500    f(x3) = 0,457
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import statistics as sts

# Dados de entrada (discretos)
data = {
    'x': [300, 400, 500],
    'y' : [0.616, 0.525, 0.457],
}
df = pd.DataFrame(data)

# Gráfico
plt.plot(df['x'],df['y'],'o',color='red', label='Dados Discretos');

# Construindo as matrizes A e b
A = np.array([[300**2, 300, 1], [400**2, 400, 1], [500**2, 500, 1]])
b = np.array([0.616, 0.525, 0.457])

def GaussIngenua(A, b):
    # Verifica se A é uma matriz quadrada
    m, n = A.shape
    if m != n:
        raise ValueError('A matriz A deve ser quadrada')

    nb = n + 1
    Aum = np.hstack((A, b.reshape(-1, 1)))

    # Eliminação progressiva
    for k in range(n - 1):
        for i in range(k + 1, n):
            fator = Aum[i, k] / Aum[k, k]
            Aum[i, k:nb] = Aum[i, k:nb] - fator * Aum[k, k:nb]

    # Substituição regressiva
    x = np.zeros(n)
    x[n - 1] = Aum[n - 1, nb - 1] / Aum[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (Aum[i, nb - 1] - np.dot(Aum[i, i + 1:n], x[i + 1:])) / Aum[i, i]

    return x

# Solução do Sistema Linear

a_i = GaussIngenua(A, b)
print("Solução:", a_i)
print()

# Gráfico
xspan = np.linspace(np.min(df['x']),np.max(df['x']),100)
yspan = a_i[0]*xspan*xspan + + a_i[1]*xspan +  a_i[2]
plt.plot(df['x'],df['y'],'o',color='red', label='Dados Discretos')
plt.plot(xspan,yspan,c='blue',linewidth=2,linestyle='-', label='Modelo Matemático')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.grid(True)
plt.show()