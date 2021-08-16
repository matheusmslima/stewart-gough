import math
import numpy as np
import matplotlib.pyplot as plt
from configuration import *
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

def ik(bPos, pPos, a, ik=True):
    """Finds leg lengths L such that the platform is in position defined by
    a = [x, y, z, alpha, beta, gamma]
    """
    phi = a[3]
    th  = a[4]
    psi = a[5]
    #Must translate platform coordinates into base coordinate system
    #Calculate rotation matrix elements
    cphi = math.cos(phi)
    sphi = math.sin(phi)
    cth  = math.cos(th)
    sth  = math.sin(th)
    cpsi = math.cos(psi)
    spsi = math.sin(psi)   
    #Hence calculate rotation matrix
    #Note that it is a 3-2-1 rotation matrix
    Rzyx = np.array([[cpsi*cth, cpsi*sth*sphi - spsi*cphi, cpsi*sth*cphi + spsi*sphi] \
                    ,[spsi*cth, spsi*sth*sphi + cpsi*cphi, spsi*sth*cphi - cpsi*sphi] \
                    ,[-sth, cth*sphi, cth*cphi]])
    #Hence platform sensor points with respect to the base coordinate system
    xbar = a[0:3] - bPos
    
    #Hence orientation of platform wrt base
    
    uvw = np.zeros(pPos.shape)
    for i in range(6):
        uvw[i, :] = np.dot(Rzyx, pPos[i, :])
        
    
    L = np.sum(np.square(xbar + uvw),1)
	
    #In the IK, the leg lengths are the length of the vector (xbar+uvw)
    return xbar#np.sqrt(L)
    
# a = np.array([5, 5, 5, np.deg2rad(15), np.deg2rad(15), np.deg2rad(15)])
# print(ik(bPos, pPos, a))