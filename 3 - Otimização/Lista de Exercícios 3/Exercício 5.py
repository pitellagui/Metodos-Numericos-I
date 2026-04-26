"""
Exercício 5:

Desenvolva um único programa no PYTHON para:

a) gerar gráficos de curvas de nível e de superfície para o campo de temperaturas:

    T(x,y) = 2x^2 + 3y^2 - 4xy - y - 3x

b) determinar o mínimo com a função minimize do PYTHON.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

# Define as variáveis x e y usando linspace
x = np.linspace(-1.75, 1.75, 100)
y = np.linspace(-1.75, 1.75, 100)

# Cria uma grade bidimensional X e Y usando meshgrid
X, Y = np.meshgrid(x, y)

# Calcula os valores da função Z para cada par de pontos (X, Y)
#Z = 2*X**2 + 3*Y**2 - 4*X*Y - Y - 3*X
Z = X**4 + Y**4 - 4*X*Y + 1


# Gráfico de contorno
fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(122)
cs = plt.contour(X, Y, Z, cmap='viridis')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid()
plt.show()


# Gráfico de superfície
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(121, projection='3d')
cs = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$T(x_1, x_2$)')
plt.show()


# Função a ser minimizada
def func(x):

    #return 2*x[0]**2 + 3*x[1]**2 - 4*x[0]*x[1] - x[1] - 3*x[0]
    #return 10*(x[0]**2)*x[1] - 5*x[0]**2 - 4*x[1]**2 - x[0]**4 - 2*x[1]**4
    #return x[0]**4 + x[1]**4 - 4*x[0]*x[1] + 1
    return (x[0] - 1)**2 + x[1]**2 + (6 - x[0] - 2*x[1])**2

# Aproximação Inicial
x0 = [1, 1]

# Minimize usando o método Nelder-Mead
res = optimize.minimize(func, x0, method='nelder-mead')

# Resultado
print(res.x)
print()