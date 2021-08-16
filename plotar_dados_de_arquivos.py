import numpy as np
import matplotlib.pyplot as plt


#my_file=open("pontos_com_rotacao3.txt","r")
# print(my_file.readlines(0))

#lines = [line.rstrip('\n') for line in my_file]
#print(lines)
#with open('pontos_com_rotacao3.txt') as f:
#    lines = f.readlines()
#    print(lines)



with open('pontos_com_rotacao5.txt') as f:
    lines = [line.rstrip() for line in f]
#print(len(lines))
#a = [np.fromstring(lines, dtype=float, sep=',') for line in lines]
		#arr = np.append(arr, a, axis=None)
pontos = np.zeros((len(lines), 3))
#print(pontos)
for i in range(len(lines)):
	a = np.fromstring(lines[i], dtype=float, sep=',')
	pontos[i] = a[:3]
	#pontos = np.append(a[:3])
	#print(pontos)
#print(pontos)



x = np.zeros(len(pontos))
y = np.zeros(len(pontos))
z = np.zeros(len(pontos))

for i in range(len(pontos)):
	x[i], y[i], z[i] = pontos[i,0], pontos[i,1], pontos[i,2]

#print(lines)
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, color="black")
plt.show()

# with open("pontos_com_rotacao4.txt", "a") as myfile1:
# 	myfile1.read("%.4f, %.4f, %.4f, %.4f, %.4f, %.4f\n" % (a[0], a[1], a[2], a[3], a[4], a[5]))

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



# plt.show()