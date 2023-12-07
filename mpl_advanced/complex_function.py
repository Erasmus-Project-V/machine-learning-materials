import numpy as np
from matplotlib import pyplot as plt, animation


## Mandelbrot set

def f(c, z):
    return z ** 2 + c




res = 15
cx = 0
cy = 0
x = np.linspace(cx-1, cx+1, res,dtype=np.float16)
y = np.linspace(cy-1, cy+1, res,dtype=np.float16)

def mb(x,y,res0):
    xx, yy = np.meshgrid(x, y)
    x0 = np.zeros(res0)
    y0 = np.zeros(res0)
    x0,y0 = np.meshgrid(x0,y0)
    iter = 0
    z = np.zeros(xx.shape)
    max_iter = 1000
    while iter < max_iter:
        xtemp = x0**2 - y0**2 + xx
        y0 = 2*x0*y0 + yy
        x0 = xtemp
        iter += 1
        z[(x0**2+y0**2)<4] += 1
    return xx,yy,z



fig = plt.figure(figsize=(20, 8))
ax1 = fig.add_axes((0.1, 0.1, 0.9, 0.9))

def zoom(res0):
    res0 = res0 +2
    ax1.cla()
    x = np.linspace(cx-2, cx+1, res0,dtype=np.float16)
    y = np.linspace(cy-1.5, cy+1.5, res0,dtype=np.float16)
    xx,yy,z = mb(x,y,res0)
    ax1.contourf(xx,yy,z)

zoom(1000)


fig.show()
