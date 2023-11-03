import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def plotScatter(X,y,model,resolution,plt):

    markers = ("o","s","^","v","<")
    colors = ("r","b","k","y","g")
    # uzmi boja kolko ti treba za tih x klasa koje imaš
    cmap = ListedColormap(colors[:len(np.unique(y))])


    # uzmemo najmanje feature vals i najveće, onda ćemo za njihovek ombinaicje ic testirat kakve su
    x1_min,x1_max = X[:,0].min() -1, X[:,0].max()+1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    #sve točke koje ćemo pregledati
    x1range = np.arange(x1_min,x1_max,resolution)
    x2range = np.arange(x2_min,x2_max, resolution)

    ## ovo daje sve moguće kommbinacije x i y, tako da se one mogu plottati, vraća 2 matrice
    xx1, xx2 = np.meshgrid(x1range,x2range)

    ## ravel doslovno flattena array, tako dobivamo sve kombinacije iz meshgrida
    reshaped = np.array((xx1.ravel(),xx2.ravel()))

    preds = model.predict(reshaped.T)
    preds = preds.reshape(xx1.shape)
    ##filled contours - countorf
    ## countors su stvari iz spatial geometry - tj- 3d funkcija ima contour lines
    plt.contourf(xx1,xx2,preds)
    plt.set_xlim(xx1.min(), xx1.max())
    plt.set_ylim(xx2.min(), xx2.max())
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=f'Class {cl}',
                    edgecolor='black')
    plt.legend(loc = "lower right")


def plot_losses(loss_list,plt):
    spacing = np.arange(0,len(loss_list),1)
    plt.bar(spacing,loss_list,width=0.5,color="r")
    plt.set_title("losses by epoch")


