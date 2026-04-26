"""
Exemplo 5:

Use os recursos gráficos do PYTHON para exibir a seguinte função e estimar
visualmente seu mínimo no intervalo -2 <= x1 <= 0 e 0 <= x2 <= 3:

    f(x1,x2) = 2 + x1 - x2 + 2x1^2 + 2x1x2 + x2^2
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Define as variáveis x e y usando linspace
x1 = np.linspace(-2, 0, 40)
x2 = np.linspace(0, 3, 40)

# Cria uma grade bidimensional X e Y usando meshgrid
X1, X2 = np.meshgrid(x1, x2)

# Calcula os valores da função Z para cada par de pontos (X, Y)
Z = 2 + X1 - X2 + 2 * X1**2 + 2 * X1 * X2 + X2**2

# Gráfico de superfície
plt.figure()
ax = plt.axes(projection='3d')
cs = ax.plot_surface(X1, X2, Z, cmap='viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2$)')
plt.show()




# Gráfico de contorno
plt.figure()
plt.contour(X1, X2, Z, cmap='viridis')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid()
plt.show()
