"""
Exercício 2:

A série infinita:

    f(n) = sum_{i=1}^{n} 1 / i^4

converge para um valor:

    f(n) = pi^4 / 90

quando n tende a infinito.

Escreva um programa para determinar o número de termos necessários
para aproximar a série até 4 algarismos.

Avalie o erro relativo percentual verdadeiro (Ept) e o erro percentual
estimado (Epest).

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
  return 1/(i**4)

# Valor Verdadeiro
u = (math.pi**4)/90

# Números de algarismos significativos
n = 4

# Critério de Scarvorought, 1966
Eppara = 0.5*10**(2-n)

# Definição das variáveis
soma = 0
v_old = 100
k = 1
Epest = v_old
estimativas = []
E_pt = []
E_pest = []
nn = []

while Epest >= Eppara:

  soma = soma + serie_de_maclaurin(x,k)
  v = soma
  v_new = soma
  if k == 1:
    Epest = 100
  else:
    Epest = abs((v_new-v_old)/v_new)*100 # Erro Percentual Estimado (%)
  v_old = v_new

  Ept = abs((u-soma)/u)*100 # Erro Percentual Verdadeiro (%)
  k = k + 1 # Contador

  # Salvando os cálculos
  nn.append(k)
  estimativas.append(soma)
  E_pest.append(Epest)
  E_pt.append(Ept)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativas
table['Epest (%)'] = E_pest
table['Ept (%)'] = E_pt
print(table)

# Gráficos

plt.plot(table['n'],table['Ept (%)'],'o--',color='blue',label='Ept (%)')
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()

