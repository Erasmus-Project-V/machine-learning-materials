import matplotlib.pyplot as plt
import numpy as np

x = ["Programer","Matematičar","Pisac","Smetlar","Kuhar"]
y = [20,40,12,43,59]
x_2 = ["Odličan","Vrlo dobar","Dobar","Dovoljan","Nedovoljan"]
y_2 = [30,10,2,43,69]
nesigurni = [9,0,3,19,1]

fig,axes = plt.subplots(figsize=(20,8),nrows=1,ncols=3)
axes[0].set_title("Buduća zanimanja učenika iz V.")
## yerr - y error ili variance
axes[0].bar(x,y,color="b",yerr=nesigurni)

axes[1].set_title("Avg ocjena učenika V. gimnazije")
## yerr - y error ili variance
axes[1].bar(x_2,y_2,color="r",)

axes[2].set_title("Usporedba")
## np.arange samo uzme intoveod 0 do range, slicno kao linspace
spacing = np.arange(0,5,1)
axes[2].bar(spacing,y,color="r",width=0.45,edgecolor="k")
axes[2].bar(spacing+0.45,y_2,width=0.45,color="b",edgecolor="k")
## sa xticks dodajemo podnaslove - plt je trenutno na axes 2, zato ovo radi
plt.xticks(spacing+0.45/2,("5/Programer","4/Matematičar","3/Pisac","2/Smetlar","1/Kuhar"))
## ADVANCED: Ako ih želimo stackati, dodamo još bottom=(y list) argument

fig.tight_layout()
fig.show()