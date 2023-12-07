import random

import numpy as np
from matplotlib import pyplot as plt, animation

ro = 10
# thetu vec imam otprije
theta = np.linspace(0, 2 * np.pi, 150)

rotations = np.linspace(0, 2 * np.pi, 150)
phi = np.linspace(0, np.pi, theta.size // 2)
u, v = np.meshgrid(theta, phi)

x2 = np.cos(u) * np.sin(v)
y2 = np.sin(u) * np.sin(v)
z2 = np.cos(v)
##  kreacija figura i osi

fig = plt.figure(figsize=(10, 10))
ax2 = fig.add_axes((0.1, 0.1, 0.9, 0.9), projection="3d")
ax2.plot_wireframe(x2, y2, z2)

##kreacija satelita

r = 1.4
det = 150
speed = 7
incl = 1
print("Orbital pollution simulator v1")
nsat = int(input("Please input number of active satelites; \n"))

incl_rot = np.pi / 6
random_inclinations = np.random.random(nsat) * np.pi / 2
random_deltas = np.random.random(nsat) * 3
random_start = np.random.random(nsat) * np.pi * 2

# random_inclinations = np.asarray([0]*nsat)
# random_deltas = np.asarray([0]*nsat)
# random_start = np.asarray([0]*nsat)


satellite_x = []
satellite_y = []
satellite_z = []
for i in range(nsat):
    s0 = speed + random_deltas[i]
    print(random_start[i])
    z = np.zeros(det) + np.sin(
        np.linspace(0, np.pi * 2 * s0, det)) * \
        np.sin(random_inclinations[i]) * r
    x = r * np.cos(np.linspace(0, 2 * np.pi * s0, det) + random_start[i])
    y = r * np.sin(np.linspace(0, 2 * np.pi * s0, det) + random_start[i])
    satellite_z.append(z)
    satellite_x.append(x)
    satellite_y.append(y)

satellite_x = np.asarray(satellite_x)
satellite_y = np.asarray(satellite_y)
satellite_z = np.asarray(satellite_z)



def refresh(frame):
    rotation = rotations[frame]
    x_r = x2 * np.cos(rotation) - y2 * np.sin(rotation)
    y_r = x2 * np.sin(rotation) + y2 * np.cos(rotation)
    ax2.cla()
    ax2.set_xlim(-1.7, 1.7)
    ax2.set_ylim(-1.7, 1.7)
    ax2.set_zlim(-1.7, 1.7)
    ax2.scatter3D(satellite_x[:, :],
                  satellite_y[:, :],
                  satellite_z[:, :], color="k", s=10)
    ax2.plot_wireframe(x_r, y_r, z2)
    return None


refresh(1)
# ani = animation.FuncAnimation(fig=fig, func=refresh, frames=150, interval=30, )

fig.show()
