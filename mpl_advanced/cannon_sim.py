import math
import time

import numpy as np
from matplotlib import pyplot as plt, animation
from scipy.spatial import distance

g = 9.81
m = 20
go = True
while go:
    F = int(input("Input force: "))
    dmass = {"small": 1.5, "medium": 5, "large": 10}
    m = dmass[input("Select shell (small,medium,large): ")]

    incl_y = int(input("provide vertical inclination (in degrees):"))
    incl_x = int(input("provide horizontal inclination (in degrees):"))
    t = 1

    vel = (F * t) / m
    print(vel)
    alpha = math.radians(incl_y)
    beta = math.radians(incl_x)
    vel_z = vel * math.sin(alpha)
    vel_hor = vel * math.cos(alpha)
    print(vel_z)

    z_impact_t = 2 * vel_z / g
    z_impact_s = vel_hor * z_impact_t
    x_impact = z_impact_s * np.cos(beta)
    y_impact = z_impact_s * np.sin(beta)

    print(z_impact_t, z_impact_s)
    times = np.linspace(0, z_impact_t, 100, dtype=np.float16)
    z_impacts = -(9.81 * times ** 2) / 2 + vel_z * times
    hor_impacts = vel_hor * times
    x_impacts = hor_impacts * np.cos(beta)
    y_impacts = hor_impacts * np.sin(beta)

    fig = plt.figure(figsize=(20, 8))
    ax1 = fig.add_axes((0.1, 0.1, 0.9, 0.9), projection="3d")

    tank_size = 20 * round(max(x_impact, y_impact) ** 0.5)
    randoms = np.random.random([2, tank_size]) * max(x_impact, y_impact) * 1.5
    z_s = np.zeros(tank_size)
    ax1.scatter(randoms[0, :], randoms[1, :], z_s, color="g", s=30)
    ax2 = fig.add_axes((0,0,0,0))
    t, = ax1.plot(x_impacts, y_impacts, z_impacts, marker=".")

    ax1.set_zlim(0, round(max(z_impacts)))


    def find_impacts(x, y, r):
        distances = ((randoms[0,:]-x)**2+(randoms[1,:]-y)**2)**0.5
        d = distances[np.where(distances<r)]
        return len(d)


    def refresh(frame):
        zs = z_impacts[:frame]
        xs = x_impacts[:frame]
        ys = y_impacts[:frame]
        t.set_data_3d(xs, ys, zs)
        if frame == len(z_impacts) - 1:
            ax1.scatter(x_impact, y_impact, 0, s=200 * m, color="r")
            ax2.text(50,100,f"hits: {find_impacts(x_impact,y_impact,m)}")
        return t


    ani = animation.FuncAnimation(fig=fig, func=refresh, frames=len(z_impacts), interval=z_impact_t * 1000 / len(z_impacts),
                                  repeat=False)

    fig.show()
    go = input("Press enter to quit...")

