"""
Exercício 1:

A série infinita:

    f(n) = sum_{i=1}^{n} 1 / i^4

converge para um valor:

    f(n) = pi^4 / 90

quando n tende a infinito.

Escreva um programa em precisão simples para calcular f(n) para n = 10.000,
calculando a soma de i = 1 a 10.000.

A seguir, repita os cálculos, de i = 10.000 até 1, usando incrementos de -1.

Em cada caso, calcule o erro relativo percentual verdadeiro.

Explique os resultados.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Definição de x
x = 1

# Definição da Função
def serie_de_maclaurin(x,i):
  return 1/i**4

# Valor Verdadeiro
u = ((math.pi)**4)/90

# Definição das variáveis
soma = 0
estimativas = []
E_pt = []
nn = []
N = 1000 # Numero máximo de iterações
for i in range(1,N+1):
  k = i  # Contador
  soma = soma + serie_de_maclaurin(x,i)
  v = soma
  v_new = soma
  Ept = abs((u-soma)/u)*100 # Erro Percentual Verdadeiro (%)

  # Salvando os cálculos
  nn.append(k)
  estimativas.append(soma)
  E_pt.append(Ept)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativas
table['Ept (%)'] = E_pt
print(table)

# Gráficos
plt.plot(table['n'],table['Ept (%)'],'o--',color='blue',label='Ept (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro (%)')
plt.legend()
plt.show()

# Definição de x
x = 1

# Definição da Função
def serie_de_maclaurin(x,i):
  return 1/i**4

# Valor Verdadeiro
u1 = ((math.pi)**4)/90

# Definição das variáveis
soma1 = 0
estimativas1 = []
E_pt1 = []
nn1 = []
N = 1000 # Numero máximo de iterações
for i in range(N,0,-1):
  k1 = (N + 1- i) # Contador
  soma1 = soma1 + serie_de_maclaurin(x,i)
  v1 = soma1
  Ept1 = abs((u1-v1)/u1)*100 # Erro Percentual Verdadeiro (%)

  # Salvando os cálculos
  nn1.append(k1)
  estimativas1.append(soma1)
  E_pt1.append(Ept1)


# Data Frame
table1 = pd.DataFrame()
table1['n'] = nn1
table1['Estimativa'] = estimativas1
table1['Ept (%)'] = E_pt1
print(table1)

# Gráficos
plt.plot(table1['n'],table1['Ept (%)'],'o--',color='blue',label='Ept (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro (%)')
plt.legend()
plt.show()