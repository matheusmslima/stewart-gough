from fk import ik
from configuration import *
import matplotlib

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



def display(bPos, pPos, a):
	r = 1.0
	theta = np.linspace(0, 2*np.pi, 1000)
	x = r * np.sin(theta)
	y = r * np.cos(theta)
	z = [1.0]*1000	


	fig = plt.figure(1)
	ax = plt.axes(projection="3d")

	# ax.set_xlim3d(-50, 50)
	# ax.set_ylim3d(-50, 50)
	# ax.set_zlim3d(-50, 50) # z da circunferencia em -800

	ax.view_init(30, 30)
	ax.scatter3D(bPos[:,0], bPos[:,1], bPos[:,2], color="black")
	ax.scatter3D(pPos[:,0], pPos[:,1], pPos[:,2] + 1.0, color="black")
	ax.scatter3D(x, y, z);

	plt.show()


a = [0,0,0.5, 0,0,0]

display(bPos, pPos, a)




# # print(type(bPos))
# pontos = [x, y, z]
# print(pontos)


a = [0,0,500, 0,0,0]
# a_result = ik(bPos, pPos, a)

# print(a_result)
# # --- #
# # PLOTAR
# # --- #

