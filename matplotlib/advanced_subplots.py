import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0,10,20)
y_1 = 2.73 ** x_1


fig_1,axes_1 = plt.subplots(figsize=(8,4), nrows=1,ncols=3)
#popravlja overlapping
plt.tight_layout()
plt.title("e^x")
#možemo acessat subplotove po indeksima
axes_1[1].set_xlabel("Plot 1")
axes_1[1].set_ylabel("Ylab")
axes_1[1].set_title("Xlab")
axes_1[1].plot(x_1,y_1)


##Appearance
## basic boje: (b:blue,g:green,c:cyan,m:magenta)
## y: yellow, k:black, w:white
## color="0.75" 75% black
## hexcodes = color="#aabbcc"
## postoje color names - wiki/Web_colors

#lw - linewidth , ls - linestyle marker - radi tockice na kordinatama x i y
axes_1[2].plot(np.log10(y_1),x_1,color='magenta',alpha=.75,lw=5,ls="-.", marker="o",markersize=10,
               markerfacecolor="y",markeredgecolor="y")



plt.show()