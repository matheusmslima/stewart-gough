import numpy as np

bb = 1
bd = 0.150

B1 = np.matrix([[  bb/2], [-(bb + 2*bd)*np.sqrt(3)/6], [0], [1]])
B2 = np.matrix([[- bb/2], [-(bb + 2*bd)*np.sqrt(3)/6], [0], [1]])
B3 = np.matrix([[- (bb/2 + bd/2)], [-(bb + 2*bd)*np.sqrt(3)/6 + bd*np.sqrt(3)/2], [0], [1]])
B4 = np.matrix([[- bd/2], [(bb + 2*bd)*np.sqrt(3)/3 - bd*np.sqrt(3)/2], [0], [1]])
B5 = np.matrix([[  bd/2], [(bb + 2*bd)*np.sqrt(3)/3 - bd*np.sqrt(3)/2], [0], [1]])
B6 = np.matrix([[ (bb + bd)/2], [-(bb + 2*bd)*np.sqrt(3)/6 + bd*np.sqrt(3)/2], [0], [1]])

sb = 0.533
sd = 0.233

P1 = np.matrix([[  sd/2],[-(sb + 2*sd)*np.sqrt(3)/3 + sd*np.sqrt(3)/2],[0],[1]])
P2 = np.matrix([[- sd/2],[-(sb + 2*sd)*np.sqrt(3)/3 + sd*np.sqrt(3)/2],[0],[1]])
P3 = np.matrix([[- (sb+sd)/2], [(sb + 2*sd)*np.sqrt(3)/6 - sd*np.sqrt(3)/2],[0],[1]])
P4 = np.matrix([[- sb/2], [(sb + 2*sd)*np.sqrt(3)/6], [0], [1]])
P5 = np.matrix([[  sb/2], [(sb + 2*sd)*np.sqrt(3)/6], [0], [1]])
P6 = np.matrix([[ (sb+sd)/2], [(sb + 2*sd)*np.sqrt(3)/6 - sd*np.sqrt(3)/2], [0], [1]])