"""
Exercício 2:

Calcule e^(-5) usando as duas abordagens:

    e^(-x) = 1 - x + (x^2)/2! - (x^3)/3! + ...

e

    e^(-x) = 1 / e^x

ou seja:

    e^(-x) = 1 / (1 + x + (x^2)/2! + (x^3)/3! + ...)

e compare com o valor verdadeiro de:

    6,737947 x 10^(-3)

Use 20 termos para calcular cada série e calcule os erros percentuais
verdadeiros quando cada termo for adicionado.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Definição de x
x = 5

# Definição da Função
def serie_de_maclaurin(x,i):
  return ((-1)**i)*(x**i)/(math.factorial(i))

# Valor Verdadeiro
u = 6.737947e-3

# Definição das variáveis
soma = 0
estimativas = []
E_pt = []
nn = []
N = 20 # Numero máximo de iterações
for i in range(0,N):
  k = i + 1 # Contador
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

# Gráficos
plt.plot(table['n'],table['Estimativa'],'o--',color='blue',label='Ept (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Estimativa')
plt.legend()
plt.show()

# Definição de x
x = 5

# Definição da Função
def serie_de_maclaurin(x,i):
  return (x**i)/(math.factorial(i))

# Valor Verdadeiro
u1 = 6.737947e-3

# Definição das variáveis
soma1 = 0
estimativas1 = []
E_pt1 = []
nn1 = []
N = 20 # Numero máximo de iterações
for i in range(0,N):
  k1 = i + 1 # Contador
  soma1 = soma1 + serie_de_maclaurin(x,i)
  v1 = 1/soma1
  Ept1 = abs((u1-v1)/u1)*100 # Erro Percentual Verdadeiro (%)

  # Salvando os cálculos
  nn1.append(k1)
  estimativas1.append(v1)
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

plt.plot(table1['n'],table1['Estimativa'],'o--',color='blue',label='Ept (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Estimativa')
plt.legend()
plt.show()