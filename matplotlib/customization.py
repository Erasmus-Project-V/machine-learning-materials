import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0,5,10)
y_1 = x_1**2


fig_1 = plt.figure(figsize=(8,5))
axes_1 = fig_1.add_axes([0.1,0.1,0.8,0.8])
axes_1.set_title("sales growth by year")
axes_1.set_xlabel("year")
axes_1.set_ylabel("Income, millions $")
axes_1.plot(x_1,y_1,color="cyan",lw=3,ls=":",marker="x",markersize=20,
            markerfacecolor="r",markeredgecolor="r")
axes_1.set_ylim([0,10])
axes_1.set_xlim([0,10])
# dashes radi tako da prvo ide len iscrtanog pa len praznog i tako unedogled
axes_1.grid(True, color="0.6", dashes=(5,2,1,2))
axes_1.set_facecolor("0.3")
plt.show()

###SPREMANJE VIZUALIZACIJE
fig_1.savefig("saved_imgs/cool_plot.png")