
"""
Exemplo 6:

Use os recursos gráficos do PYTHON para exibir a seguinte função e estimar
visualmente seu mínimo no intervalo -2 <= x1 <= 0 e 0 <= x2 <= 3:

    f(x1,x2) = 2 + x1 - x2 + 2x1^2 + 2x1x2 + x2^2
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize


# Função a ser minimizada
def func(x):
    return 2 + x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2

# Aproximação Inicial
x0 = [-0.5, 0.5]

# Minimize usando o método Nelder-Mead
res = optimize.minimize(func, x0, method='nelder-mead')

# Resultado
print(res)
print()