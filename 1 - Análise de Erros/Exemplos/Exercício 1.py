"""
Exercício 1:

Escreva um programa para obter a estimativa de e^x do Exemplo 1.
Verifique para x = 1 e escolha outro valor qualquer para x.
Análise e explique os resultados.

Exemplo 1:

Calcule e^x, considerando x = 1, usando a aproximação por série de Maclaurin:

    e^x = 1 + x + (x^2)/2! + (x^3)/3! + ... + (x^n)/n! + ...

e compare com o valor verdadeiro de:

    e^1 = e = 2,71828182846...

Use 6 termos para calcular uma aproximação da série e calcule
os erros relativos aproximados e verdadeiros quando cada termo for adicionado.
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


# Valor Verdadeiro
u = 2.71828182846

# Definição das variáveis
soma = 0
v_old = 100
estimativas = []
E_pt = []
E_pest = []
nn = []
N = 6  # Numero máximo de iterações
for i in range(0, N):
    k = i + 1  # Contador
    soma = soma + serie_de_maclaurin(x, i)
    v = soma
    v_new = soma
    Ept = abs((u-soma)/u)*100  # Erro Percentual Verdadeiro (%)
    if i == 0:
        Epest = 100
    else:
        Epest = abs((v_new - v_old)/v_new)*100  # Erro Percentual Estimado (%)
    v_old = v_new

    # Salvando os cálculos
    nn.append(k)
    estimativas.append(soma)
    E_pt.append(Ept)
    E_pest.append(Epest)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativas
table['Ept (%)'] = E_pt
table['Epest (%)'] = E_pest
print(table)

# Gráficos
plt.plot(table['n'], table['Ept (%)'], 'o--', color='blue', label='Ept (%)')
plt.plot(table['n'], table['Epest (%)'], 'o--', color='red', label='Epest (%)')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Percentual Verdadeiro ou Estimado (%)')
plt.legend()
plt.show()