"""
Exercício 2:

Escreva um programa para obter a estimativa de e^x (Exemplo 1)
considerando o Critério de Parada de Scarvorought (1966) com n = 4.

Verifique para x = 1 e escolha outro valor qualquer para x.
Análise e explique os resultados.

Exemplo 1:

Calcule e^x, considerando x = 1, usando a aproximação por série de Maclaurin:

    e^x = 1 + x + (x^2)/2! + (x^3)/3! + ... + (x^n)/n! + ...

e compare com o valor verdadeiro de:

    e^1 = e = 2,71828182846...
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Definição de x
x = 1

# Definição da Função
def serie_de_maclaurin(x, i):
    return (x**i)/math.factorial(i)

# Números de algarismos significativos
n = 4

# Critério de Scarvorought, 1966
Eppara = 0.5 * 10**(2-n)

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

    soma = soma + serie_de_maclaurin(x, k)
    v_new = soma
    if k == 0:
        Epest = 100
    else:
        Epest = abs((v_new-v_old)/v_new)*100  # Erro Percentual Estimado (%)
    v_old = v_new
    k = k + 1  # Contador

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
plt.plot(table['n'], table['Epest (%)'], 'o--', color='red', label='Epest (%)')
plt.xlabel(' Número de Iterações')
plt.ylabel('Erro Percentual Estimado (%)')
plt.legend()
plt.show()
