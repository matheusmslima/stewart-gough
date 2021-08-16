from fk import ik
from configuration import *
import matplotlib

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

array_comprimentos = np.zeros(1000)
comprimentos = open("comprimentos_sg.txt", "r")
lista_comprimentos = [0]*1000
print(lista_comprimentos)
print(comprimentos.readlines()[9])

for i in range(1000):
	lista_comprimentos[i] = comprimentos.readlines()[i]
print(lista_comprimentos)