import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 10, 20)
y_1 = x_1 ** 1.5

## figure je nešto kao window - on samo postoji - figsize je u inčima
fig_1 = plt.figure(figsize=(5, 4))
## axes je stvar po kojoj se crta - koord sustav ajmorec --u listi je axes size
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
# title ide na axes i ovo ostalo
axes_1.set_xlabel("Days")
axes_1.set_ylabel("Months")
axes_1.set_title("Graph")
# na axes mozemo plotati prozivaljan broj elemenata!
axes_1.plot(x_1, y_1, label="x^1.5")
axes_1.plot(y_1, x_1, label="x^1/1.5")
## Dodaje legendu sa labelima
## loc=0 gore desno 1 gore ljevo 2 dolje 3 i 4 ili tuple (x,y)
axes_1.text(1, 1, "intercept=1")
axes_1.legend(loc=0)

##Hiptotetski mogu dodati jos jedan axis u figuru ali necu da bude uredno

fig_1.show()
