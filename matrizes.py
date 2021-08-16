import numpy as np

def skew(arr):
 	return np.matrix([[      0, -arr[2],  arr[1], 0],
 					 [ arr[2],       0, -arr[0], 0],
 					 [-arr[1],  arr[0],      0, 0],
 					 [0, 0, 0, 0]])


def Rx(alpha):
	return np.matrix([[1, 0, 0, 0],
					 [0, np.cos(alpha), -np.sin(alpha), 0],
					 [0, np.sin(alpha),  np.cos(alpha), 0],
					 [0, 0, 0, 1]])

def Ry(beta):
	return np.matrix([[ np.cos(beta), 0, np.sin(beta), 0],
					 [ 0, 1, 0, 0],
					 [-np.sin(beta), 0, np.cos(beta), 0],
					 [ 0, 0, 0, 1]])

def Rz(gamma):
	return np.matrix([[ np.cos(gamma), -np.sin(gamma), 0, 0],
					 [ np.sin(gamma),  np.cos(gamma), 0, 0],
					 [ 0, 0, 1, 0],
					 [ 0, 0, 0, 1]])

def Tx(dx):
	return np.matrix([[1, 0, 0, dx],
					 [0, 1, 0,  0],
					 [0, 0, 1,  0],
					 [0, 0, 0,  1]])
def Ty(dy):
	return np.matrix([[1, 0, 0,  0],
					 [0, 1, 0, dy],
					 [0, 0, 1,  0],
					 [0, 0, 0,  1]])

def Tz(dz):
	return np.matrix([[1, 0, 0,  0],
					 [0, 1, 0,  0],
					 [0, 0, 1, dz],
					 [0, 0, 0,  1]])

def Transl(dx, dy, dz):
	return np.matrix([[1, 0, 0,  dx],
					 [0, 1, 0,  dy],
					 [0, 0, 1,  dz],
					 [0, 0, 0,  1]])