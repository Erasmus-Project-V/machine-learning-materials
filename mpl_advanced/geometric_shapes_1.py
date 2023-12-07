import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

## konus i oktahedron

# konus je radi korijena problematican u kartezijanskom sustavu sa compl. vals
# stoga koristim sferni polarni sustav - konus je definiran funkcijom:
# theta = alfa (konst.)

detail = 100
theta = np.linspace(0,2*np.pi,detail)
phi = np.ones(detail)*np.pi/6

ro = np.linspace(0,100,detail)

theta,ro = np.meshgrid(theta,ro)
x = ro*np.cos(theta) * np.sin(phi)
y = ro*np.sin(theta) * np.sin(phi)
z = ro*np.cos(phi)
z2 = ro*-np.cos(phi)

from mpl_toolkits import mplot3d
from itertools import permutations
from scipy.spatial import ConvexHull,distance


# octahedron
perms = ((0,1,2),(0,1,-2),(0,-1,2),(0,-1,-2))
iters = []
for p0 in perms:
    p = permutations(p0)
    for p1 in p:
        iters.append(p1)
iters = list(sorted(iters))
iters = np.asarray([np.asarray(d) for d in iters])
print(iters)



fig = plt.figure(figsize=(20,8))
ax1 = fig.add_axes((0.1,0.1,0.5,0.9),projection="3d")
ax2 = fig.add_axes((0.5,0.1,0.5,0.9),projection="3d")
ax1.plot_surface(x,y,z)
ax1.plot_surface(x,y,z2)

hull = ConvexHull(iters)
for s in hull.simplices:
    tri = Poly3DCollection([iters[s]])
    tri.set_color("b")
    tri.set_alpha(0.5)
    tri.set_edgecolor("none")
    ax2.add_collection3d(tri)
    edges = []
    distances = sorted([(distance.euclidean(iters[s[0]],iters[s[1]]),(s[0],s[1])),
                        (distance.euclidean(iters[s[1]],iters[s[2]]),(s[1],s[2])),
                        (distance.euclidean(iters[s[0]],iters[s[2]]),(s[2],s[0]))])
    mind = distances[0][0]
    edges.append(distances[0][1])
    if distances[1][0] == mind:
        edges.append(distances[1][1])
    for v0, v1 in edges:
        ax2.plot3D(xs=[iters[v0, 0],iters[v1, 0]],
                 ys=[iters[v0, 1],iters[v1, 1]],
                 zs=[iters[v0, 2],iters[v1, 2]],
                 color='k')





ax2.scatter(iters[:,0],iters[:,1],iters[:,2],color="k")


fig.show()
