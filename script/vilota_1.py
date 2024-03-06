import numpy as np
from spatialmath import *
from math import pi

import matplotlib.pyplot as plt

# Create a identity SE(3) Transformation
Ha = SE3(0,0,0) 

# A transformation that only translates along the x axis and y axis
Hb = SE3(2,0.5, 0)

# A transformation that rotates 45 degree about x axis, 45 about y axis, then -45 about z axis
Hc = SE3.Tx(1.0) * SE3.Ty(1.0) * SE3.Tz(2) * SE3.Rz(-45, 'deg')* SE3.Ry(45, 'deg')* SE3.Rx(45, 'deg')

# A transformation that does the Hc transformation, then move along the x axis of Hc coordinate for 1
Hd = Hc * SE3.Tx(1.0)

### Animation
Ha.plot(frame='A', color='black', dims=[0,4])
Hb.plot(frame='B', color='blue', dims=[0,4])
Hb.animate(frame = 'B')
plt.show()
Ha.plot(frame='A', color='black', dims=[0,4])
Hc.plot(frame='C', color='green', dims=[0,4])
Hc.animate(frame = 'C')
plt.show()
Ha.plot(frame='A', color='black', dims=[0,4])
Hc.plot(frame='C', color='green', dims=[0,4])
Hd.plot(frame='D', color='red', dims=[0,4])
Hd.animate(frame = 'D')
plt.show()