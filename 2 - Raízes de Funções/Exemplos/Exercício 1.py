"""
Exercício 1:

Escreva um programa que emprega os seguintes métodos para encontrar
as raízes da função:

    f(x) = x^2 - 2

Métodos:

1) Método gráfico
2) Busca incremental
3) Método da bisseção
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

A = np.array([[1, 2],[3, 4]])
print(A)
print()


# Definição da função e o intervalo
def func(x):
  return x**2 - 2

xmin = -4
xmax = 4

# Gráfico
x = np.linspace(xmin,xmax,100)
plt.plot(x,func(x),'-',color='blue',label='f(x)')
plt.plot(np.linspace(xmin,xmax,100),np.linspace(0,0,100),'--',color='black')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid()
plt.show()

def busca_inc(func, xmin, xmax, ns):
    # Busca incremental
    x = np.linspace(xmin, xmax, ns)
    f = func(x)
    nb = 0
    xb = []

    # xb é nulo a menos que seja detectada mudança de sinal
    for k in range(len(x) - 1):
        if np.sign(f[k]) != np.sign(f[k + 1]):
            nb += 1
            xb.append([x[k], x[k + 1]])

    if not xb:
        # Exibe que nenhum subintervalo foi encontrado
        print('Nenhum subintervalo encontrado')
        print('Verifique o intervalo ou aumente ns')
    else:
        # Exibe o número de subintervalos
        print('Número de subintervalos:')
        print(nb)
    print()

    return np.array(xb)

def bissec(func, xl, xu, Eppara, maxit, *args):

    if func(xl, *args) * func(xu, *args) > 0:
        raise ValueError('Não há mudança de sinal')

    iter = 0
    xr_new = xl
    nn = []
    estimativa = []
    E_pest = []
    Epest = 100
    k = 0

    while Epest > Eppara or iter > maxit:
        xr_old = xr_new
        xr_new = (xl + xu) / 2
        iter += 1

        if xr_new != 0:
           Epest = abs((xr_new - xr_old) / xr_new) * 100

        test = func(xl, *args) * func(xr_new, *args)

        if test < 0:
            xu = xr_new
        elif test > 0:
            xl = xr_new
        else:
            Epest = 0

        k = k + 1 # Contador

        # Salvando o número de iterações e as estimativas dos erros
        nn.append(k)
        estimativa.append(xr_new)
        E_pest.append(Epest)

    raiz = xr_new

    fx = func(xr_new, *args)

    return raiz, fx, Epest, iter, nn, estimativa, E_pest

# Busca Incremental
ns = 100
subintervalos = busca_inc(func, xmin, xmax,ns)
print('Subintervalos:', subintervalos)
print()

# Plotar a função
x_vals = np.linspace(xmin, xmax, 1000)
y_vals = func(x_vals)
plt.plot(x_vals, y_vals, color='g', linestyle='-', label='Função')
plt.plot(np.linspace(xmin,xmax,50),np.linspace(0,0,50),linestyle='-',linewidth=0.5,color='black')
# Destacar os intervalos encontrados
for intervalo in subintervalos:
    plt.axvline(intervalo[0], color='r', linestyle='--')
    plt.axvline(intervalo[1], color='r', linestyle='--')

plt.title('Gráfico da Função com Intervalos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Critério de Scarvorought, 1966
n = 12 # Números de algarismos significativos
Eppara = 0.5*10**(2-n)

# Número Máximo de Iterações
maxit = 100
tam = len(intervalo)
for i in range(0,tam):
  # Intervalo
  xl = subintervalos[i,0]
  xu = subintervalos[i,1]
  [x, fx, Epest, iter, nn, estimativa, E_pest] = bissec(func, xl, xu, Eppara, maxit)


  print('raiz:', x)
  print('Epest:', Epest)
  print('Número de iterações:', iter)
  print()

