"""
Exemplo 5:

Use o método de Gauss-Seidel para obter a solução para:

    2x1 + 4x2 - 6x3 = 10

    4x1 + 2x2 + 2x3 = 16

    2x1 + 8x2 - 4x3 = 24
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Gauss_Seidel(A, b, x0, Eppara, maxit):
    ne = len(b)
    x = np.zeros(ne) if x0 is None else np.array(x0)


    iter = 0
    n = []
    estimativa = []
    E_pest = []
    Epest = np.linspace(100,100,ne)
    iteracoes = []

    while np.max(Epest) >= Eppara: #and iter <= maxit:
        x_old = np.copy(x)

        for i in range(ne):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Critério de parada
        Epest = np.abs((x - x_old) / x) * 100

        iter += 1

        # Salvando o número de iterações e as estimativas dos erros
        iteracoes.append(iter)
        estimativa.append(x.copy())
        E_pest.append(Epest)

    return x, iteracoes, estimativa, E_pest

'''
def TDMA(A,b):
    """
    Tridiag: Solução de sistemas de equações tridiagonais.

    x = tridiag(e, f, g, r): Solução de sistemas de equações tridiagonais.

    Entrada:
        e: vetor subdiagonal
        f: vetor diagonal
        g: vetor superdiagonal
        r: vetor do lado direito

    Saída:
        x: vetor solução
    """
    n = len(f)
    x = [0] * n

    # eliminação progressiva
    for k in range(1, n):
        factor = e[k] / f[k - 1]
        f[k] -= factor * g[k - 1]
        r[k] -= factor * r[k - 1]

    # substituição regressiva
    x[-1] = r[-1] / f[-1]
    for k in range(n - 2, -1, -1):
        x[k] = (r[k] - g[k] * x[k + 1]) / f[k]

    return x
'''


# Exemplo de uso:
A = np.array([[2, 4, -6], [4, 2, 2], [2, 8, -4]])
b = np.array([10, 16, 24])

# Critério de Scarvorought, 1966
n = 12 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 1000

# Chute Inicial
x0 = None

[x, iteracoes, estimativa, E_pest] = Gauss_Seidel(A, b, x0, Eppara, maxit)
print("Solução:", x)
print()

# Data Frame
table = pd.DataFrame()
table['Iterações'] = iteracoes
table['Estimativas'] = estimativa
table['Epest (%)'] = E_pest
print(table)
print()