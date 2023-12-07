import math

import matplotlib.pyplot as plt

import numpy as np
from matplotlib import animation

fig = plt.figure(figsize=(20, 8))
ax = fig.add_axes((0.1, 0.1, 0.5, 0.8))

radius = 1
theta = np.linspace(0, 2 * np.pi, 100)

x = radius * np.cos(theta)
y = radius * np.sin(theta)

atan_values = np.asarray([math.atan(theta[i]) for i in range(theta.size)])
module_checks = (x ** 2 + y ** 2) ** 0.5

radii_for_pointer_1 = np.linspace(0, 1, 100)
x2 = radii_for_pointer_1 * np.cos(theta).reshape(-1, 1)
y2 = radii_for_pointer_1 * np.sin(theta).reshape(-1, 1)

pl1, = ax.plot(x[0], y[0], color="b")
pl2, = ax.plot(x2[0, :], y2[0, :], color="y")



ax.set_ylim(-1.5, 1.5)
ax.set_xlim(-1.5, 1.5)

ax.grid(True,which="both")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

lx, = ax.plot(x2[0, :], [0]*100, color="r")
ly, = ax.plot([0]*100, y2[0, :], color="g")

tx_1 = ax.text(2,0.5,r'$\Theta='+str(round(theta[0]*180/np.pi))+"\degree$",size=20)
tx_2 = ax.text(2,0.65,r'$x = rcos('+str(round(theta[0]*180/np.pi))+"\degree)$",size=20)
tx_3 = ax.text(2,0.8,r'$y = rsin('+str(round(theta[0]*180/np.pi))+"\degree)$",size=20)

tx_4 = ax.text(2,0.3,r"$\Theta = atan(\frac{y}{x})$",size=20)

tx_5 = ax.text(2,0.15,r"$z = x + yi$",size=20)
tx_6 = ax.text(2,0.0,r"$Polarna \ forma:$",size=20)

tx_7 = ax.text(2,-0.15,r"$z= rcos(\Theta) + rsin(\Theta)i$",size=20)


def update(frame):
    pl1.set_xdata(x[:frame])
    pl1.set_ydata(y[:frame])

    pl2.set_xdata(x2[frame - 1, :])
    pl2.set_ydata(y2[frame - 1, :])

    lx.set_xdata(x2[frame-1, :])
    ly.set_ydata(y2[frame-1, :])
    ly.set_xdata([x2[frame-1,x2.shape[0]-1]]*100)

    tx_1.set_text(r'$\Theta='+str(round(theta[frame]*180/np.pi))+"\degree$")
    tx_2.set_text(r'$x = rcos(\Theta) = ' +
                str(round(math.cos(theta[frame]),3))+"$")
    tx_3.set_text(r'$y = rsin(\Theta) = ' +
                str(round(math.sin(theta[frame]),3))+"$")
    return (pl1, pl2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=100)
fig.show()

print("done")
