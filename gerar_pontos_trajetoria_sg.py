from fk import ik
from configuration import *
import matplotlib

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

r = 1.0
theta = np.linspace(0, 2*np.pi, 1000)

x = r * np.sin(theta)
y = r * np.cos(theta)
z = [1.0]*1000	
alpha = [0]*1000
beta = [0]*1000
gamma = [0]*1000

# pontos = [x, y, z, alpha, beta, gamma]
pontos = []

for i in range(1000):
	pontos.append([x[i], y[i], z[i], alpha[i], beta[i], gamma[i]])



comprimentos = []

for i in range(1000):
	comprimentos.append(ik(bPos, pPos, pontos[i]))

print(comprimentos[0][:])

with open("pontos_sg.txt", mode='w') as file:
    for i in range(1000):
        file.write("{:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(x[i], y[i], z[i], alpha[i], beta[i], gamma[i]))
file.close()

with open("comprimentos_sg.txt", mode='w') as file:
    for i in range(1000):
        file.write("{:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}, {:.4f}\n".format(comprimentos[i][0], comprimentos[i][1], comprimentos[i][2], \
        																	 comprimentos[i][3], comprimentos[i][4], comprimentos[i][5]))
file.close()