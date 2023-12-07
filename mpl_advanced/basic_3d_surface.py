import matplotlib.pyplot as plt
import numpy as np



# detail - kolko samplinga se uzima, ovdje 100*100
detail = 100

#otkud dokud se crta funkcija?
#ovo je arrangement za kockastu bazu crtanja

min = -10
max = 10

x = np.linspace(min, max, detail)
y = np.linspace(max, min, detail).reshape(-1, 1)

#grid xy koordinata- kockast
x, y = np.meshgrid(x, y)



# jednaždba
z = (x**2 + y**2).reshape(-1)
x = x.reshape(-1)
y = y.reshape(-1)
from mpl_toolkits import mplot3d

#prebacivanje baze u kružnicu po formuli x^^2 + y^^2 <r
z[x**2+y**2>max**2] = np.nan

r = 10
theta = np.linspace(0,2*np.pi,150)

a = r* np.cos(theta)
b = r* np.sin(theta)
z0 = 100


print(a,b,z0)

# jednažba 2 - kružnica u 3d - polarne koordinate

ro = 10
#thetu vec imam otprije

phi = np.linspace(0,np.pi,theta.size//2)
u, v = np.meshgrid(theta,phi)
x2 = np.cos(u)*np.sin(v)
y2 = np.sin(u)*np.sin(v)
z2 = np.cos(v)
##  kreacija figura i osi


fig = plt.figure(figsize=(20,8))
ax1 = fig.add_axes((0.1,0.1,0.5,0.9),projection="3d")
ax2 = fig.add_axes((0.5,0.1,0.5,0.9),projection="3d")
ax1.plot3D(x,y,z,color="b")
ax1.plot3D(a,b,z0,color="b")

ax2.plot_wireframe(x2,y2,z2)
fig.show()
