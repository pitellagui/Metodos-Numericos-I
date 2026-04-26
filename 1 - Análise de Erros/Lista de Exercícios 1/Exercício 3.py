"""
Exercício 3:

Determine o número de termos necessários para aproximar cos(x) até
8 algarismos significativos usando a aproximação por série de Maclaurin:

    cos(x) = 1 - (x^2)/2! + (x^4)/4! - (x^6)/6! + (x^8)/8! - ...

Calcule a aproximação usando um valor de:

    x = 0,3π
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Definição de x
x = 0.3*(math.pi)

# Definição da Função
def serie_de_maclaurin(x,i):
  return ((-1)**(i))*(x**(2*i))/math.factorial(2*i)

# Números de algarismos significativos
n = 8

# Critério de Scarvorought, 1966
Eppara = 0.5*10**(2-n)

# Definição das variáveis
soma = 0
v_old = 100
k = 0
Epest = v_old
estimativas = []
E_pt = []
E_pest = []
nn = []

while Epest >= Eppara:

  soma = soma + serie_de_maclaurin(x,k)
  v_new = soma
  if k == 0:
    Epest = 100
  else:
    Epest = abs((v_new-v_old)/v_new)*100 # Erro Percentual Estimado (%)
  v_old = v_new
  k = k + 1 # Contador

  # Salvando os cálculos
  nn.append(k)
  estimativas.append(soma)
  E_pest.append(Epest)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativas
table['Epest (%)'] = E_pest
print(table)

# Gráficos
plt.plot(table['n'],table['Epest (%)'],'o--',color='red',label='Epest (%)')
plt.xlabel(' Número de Iterações')
plt.ylabel('Erro Percentual Estimado (%)')
plt.legend()
plt.show()