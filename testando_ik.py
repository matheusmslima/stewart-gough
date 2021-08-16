from fk import ik
from configuration import *
import matplotlib

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


# x, y, z = bPos[:,0], bPos[:,1], bPos[:,2]
# print(bPos)
# print("\n x:{} \n y:{} \n z:{}".format(x, y, z))

r = 100
theta = np.linspace(0, 2*np.pi, 1000)
x = r * np.sin(theta)
y = r * np.cos(theta)
z = [500]*1000

print(x, y, z)
fig = plt.figure(1)
ax = plt.axes(projection="3d")

# ax.set_xlim3d(-50, 50)
# ax.set_ylim3d(-50, 50)
# ax.set_zlim3d(-50, 50) # z da circunferencia em -800

ax.view_init(30, 30)
ax.scatter3D(bPos[:,0], bPos[:,1], bPos[:,2], color="black")
ax.scatter3D(x, y, z);

plt.show()



# print(type(bPos))
pontos = [x, y, z]
print(pontos)


a = [0,0,500, 0,0,0]
a_result = ik(bPos, pPos, a)

print(a_result)
# --- #
# PLOTAR
# --- #

