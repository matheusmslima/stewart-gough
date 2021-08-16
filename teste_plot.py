# Libraries
import numpy as np
import matplotlib.pyplot as plt
from fk import ik, fk




import numpy as np
import math

#define coord system origin as the centre of the bottom plate
#Find base plate attachment locations
bAngles = [15, 105, 135, 225, 255, 345]
bAngles = [math.radians(x) for x in bAngles]
bR = 0.5
bPos = np.array([[bR*math.cos(theta), bR*math.sin(theta), 0] for theta in bAngles])


pAngles = [45, 75, 165, 195, 285, 315]
pAngles = [math.radians(x) for x in pAngles]
pR = 0.5 # radius of the end effector platform
pPos = np.array([[pR*math.cos(theta), pR*math.sin(theta), 0] for theta in pAngles])

#print(pPos)
#mod_pPos_0 = np.sqrt((pPos[0,0]**2) + (pPos[0,1]**2) + (pPos[0,2]**2))
#print(mod_pPos_0)


xb = bPos[:,0]
yb = bPos[:,1]
zb = bPos[:,2]

alpha = np.deg2rad(30)
beta  = np.deg2rad(45)
gamma = np.deg2rad(30)

a = np.array([10,450,250,alpha,beta,gamma])#np.deg2rad(15), np.deg2rad(15), np.deg2rad(15)])
ponto = ik(bPos, pPos, a)
print(ponto)

# ponto = [0.6484, 0.9988, 0.8865, 0.7777, 0.6875, 1.0302]
# # Create dataset
# bars = ('A', 'B', 'C', 'D', 'E', 'F')
# x_pos = np.arange(len(ponto))
 
# # Create bars
# plt.bar(x_pos, ponto)
 
# # Create names on the x-axis
# plt.xticks(x_pos, bars)
 
# # Show graphic
# plt.show()







#print(ponto)

#xp = ponto[:,0]
#yp = ponto[:,1]
#zp = ponto[:,2]
xp = ponto[:,0]
yp = ponto[:,1]
zp = ponto[:,2]


print("\nValor de pPos[:,0]:  %s" % pPos[:,0])
print("\nValor de ponto[:,0]: %s" % ponto[:,0])
print("\nValor de xp:         %s\n" % xp)

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot( projection='3d')


ax.scatter(xb,yb,zb, color="black") # plot the point (2,3,4) on the figure
ax.scatter(xp,yp,zp, color="black") # plot the point (2,3,4) on the figure
ax.plot_trisurf(xb, yb, zb, alpha = 0.5, color = 'grey', antialiased=True)#cmap='viridis', edgecolor='none');
ax.plot_trisurf(xp, yp, zp, alpha = 0.5, color = 'grey', antialiased=True)#cmap='viridis', edgecolor='none');

for i in range(len(xp)):
	x = [xb[i], xp[i]]
	y = [yb[i], yp[i]]
	z = [zb[i], zp[i]]
	ax.plot(x, y, z, c='b')

ax.set(xlabel='x', ylabel='y', zlabel='z')
#ax.plot_trisurf(xb, yb, zb, linewidth=0.5, antialiased=True, color="grey")
# ax.plot_trisurf(xp, yp, zp, linewidth=0.5, antialiased=True)


# plt.show()