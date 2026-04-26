"""
Exemplo 4:

Empregue a função fmindound do PYTHON para determinar o mínimo da função:

    f(x) = 2x + 3/x
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

# Intervalo
xl = 0
xu = 5

# Critério de Scarvorought, 1966
n = 6 # Números de algarismos significativos
Eppara = 0.5 * 10**(2 - n)

# Número Máximo de Iterações
maxit = 500

def func(x):
    return 2*x+3/x

# Busca do mínimo pela fmindound
xopt = optimize.fminbound(func, xl, xu, args=(), xtol=Eppara, maxfun=maxit)
print(xopt)
print()



# Gráfico
x = np.linspace(-10,10,100)
plt.plot(x,func(x),'-',color='blue',label='fx)')
plt.plot(xopt,func(xopt),'or',label='Ótimo Local')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()