
"""
Exemplo 1:

Faça uma busca incremental para identificar os subintervalos nos quais ocorre
mudança de sinal dentro do intervalo [3,6] para a função:

    f(x) = sin(10x) + cos(3x)
"""
import numpy as np
import math
import matplotlib.pyplot as plt

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

# Exemplo de uso:
def exemplo_func(x):
  return np.sin(10*x) + np.cos(3*x)

xmin = 3
xmax = 6
ns = 50
subintervalos = busca_inc(exemplo_func, xmin, xmax,ns)
print('Subintervalos:', subintervalos)
print()

# Plotar a função
x_vals = np.linspace(xmin, xmax, 1000)
y_vals = exemplo_func(x_vals)
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