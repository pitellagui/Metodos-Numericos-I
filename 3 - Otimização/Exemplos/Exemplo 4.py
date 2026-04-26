"""
Exemplo 4:

Use Função do Python: fminbound para achar o mínimo de:

    f(x) = x^2/10 - 2sin(x)

no intervalo entre xl = 0 e xu = 4.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

# Intervalo
xl = 0
xu = 4

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 500

def func(x):
    return (x**2) / 10 - 2 * np.sin(x)

# Busca do mínimo pela fmindound
xopt = optimize.fminbound(func, xl, xu, args=(), xtol=Eppara, maxfun=maxit)
print(xopt)
print()



# Gráfico
x = np.linspace(xl,xu,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')
plt.plot(xopt,func(xopt),'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()