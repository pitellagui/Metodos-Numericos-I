"""
Segundo estudos médicos um saltador de bungee jumping pode sofrer uma lesão
nas vértebras se a velocidade de queda livre exceder 36 m/s após 4 s de queda livre.
Determinar a massa (m) para qual este critério é excedido dado um coeficiente
de arraste de c_d = 0,25 kg/m.

O modelo matemático a seguir prevê a velocidade de queda em função do tempo:

    v(t) = sqrt((g*m)/c_d) * tanh( sqrt((g*c_d)/m) * t )

Para determinar m podemos reescrever a função como:

    f(m) = sqrt((g*m)/c_d) * tanh( sqrt((g*c_d)/m) * t ) - v(t)
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Dados de Entrada
v = 36 # m/s
g = 9.81 # m/s
t = 4 # s
c_d = 0.25 # kg/m

# Gráfico
m = np.linspace(0,200,100)
plt.plot(m,np.sqrt((g*m)/c_d)*np.tanh(np.sqrt((g*c_d)/m)*t)-v,'-',color='blue',label='f(m)')
plt.plot(np.linspace(100,200,100),np.linspace(0,0,100),'--',color='black')
plt.plot(np.linspace(140,140,100),np.linspace(-1.5,1.5,100),'--',color='red')
plt.plot(np.linspace(150,150,100),np.linspace(-1.5,1.5,100),'--',color='red')
plt.legend()
plt.ylabel('f(m)')
plt.xlabel('m (kg)')
plt.ylim([-1,1])
plt.xlim([100,200])
plt.grid()
plt.show()