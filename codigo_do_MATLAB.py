# importacoes

import numpy as np
import matplotlib.pyplot as plt
from matrizes import *
from configupracao_stewart import *

np.set_printoptions(precision = 4)
np.set_printoptions(suppress = True)

base_points = np.array([B1, B2, B3, B4, B5, B6])
plat_points = np.array([P1, P2, P3, P4, P5, P6])

def calc_pos(arr):
	dx, dy, dz         = arr[0], arr[1], arr[2]
	alpha, beta, gamma = arr[3], arr[4], arr[5]

	T = Transl(dx, dy, dz) * Rx(alpha) * Ry(beta) * Rz(gamma)
	return T

def comp_atuadores(Pm):
	L = np.zeros(6)	
	for i in range(6):
		qv = base_points[i] - Pm[i]
		q  = np.sqrt(np.matrix(qv).H*qv)
		L[i] = q
	return L

# a = np.array([0.2, 0.3, 0.6, 0.2, 0.3, 0.6])
# T = calc_pos(a)
# Pm = np.array([T*P1, T*P2, T*P3, T*P4, T*P5, T*P6])

# Translacao em x, y e z de 1 ate 1.5 com passo de 0.1
# Rotacao em x, y, z de 0° ate 45° com passo de 0.1

for i in np.arange(0, 1.1, 0.1):
	for j in np.arange(0, 1.1, 0.1):
		for k in np.arange(1, 2.1, 0.1):
			for alpha in np.arange(0.0, 0.8, 0.1):
				for beta in np.arange(0.0, 0.8, 0.1):
					for gamma in np.arange(0.0, 0.8, 0.1):
						a = np.array([i, j, k, alpha, beta, gamma])
						T = calc_pos(a)
						Pm = np.array([T*P1, T*P2, T*P3, T*P4, T*P5, T*P6])
						L = comp_atuadores(Pm)
						with open("pontos_com_rotacao5.txt", "a") as myfile1:
							myfile1.write("%.4f, %.4f, %.4f, %.4f, %.4f, %.4f\n" % (a[0], a[1], a[2], a[3], a[4], a[5]))
						with open("comprimentos_com_rotacao5.txt", "a") as myfile2:
							myfile2.write("%.4f, %.4f, %.4f, %.4f, %.4f, %.4f\n" % (L[0], L[1], L[2], L[3], L[4], L[5]))

# VERIFICAR DADOS DE Q1V COM OS DO MATLAB
# a = np.array([0,0,1,0,0,0])
# T = calc_pos(a)
# Pm = np.array([T*P1, T*P2, T*P3, T*P4, T*P5, T*P6])
# P1m = T*P1
# print(P1m)
# q1v = B1 - P1m
# print(np.matrix(q1v))
# # L = comp_atuadores(Pm)
# # print(L)


# qv = base_points[0] - Pm[0]
# q  = np.sqrt(np.matrix(qv).H*qv)











# fig = plt.figure(figsize=(6,6))
# ax = fig.add_subplot( projection='3d')

# for i in range(6):
# # 	ppx = plat_points[i,0]
# # 	ppy = plat_points[i,1]
# # 	ppz = plat_points[i,2]
# 	bpx = base_points[i,0]
# 	bpy = base_points[i,1]
# 	bpz = base_points[i,2]
# 	ax.scatter(bpx, bpy, bpz, color="black")
# 	ax.scatter(Pm[i,0], Pm[i,1], Pm[i,2], color="r")

# 	x = [float(base_points[i,0]), float(Pm[i,0])]
# 	y = [float(base_points[i,1]), float(Pm[i,1])]
# 	z = [float(base_points[i,2]), float(Pm[i,2])]
# 	ax.plot(x, y, z, c='b')



#plt.show()

