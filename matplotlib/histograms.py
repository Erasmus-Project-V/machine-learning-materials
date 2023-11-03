import matplotlib.pyplot as plt
import numpy as np

# histogram - graf distribucije numeričkih podataka


dice_1 = np.random.randint(1,7,7000)
dice_2 = np.random.randint(1,7,7000)
sum_of_dice = dice_1+dice_2

for_plot = list()
for i in range(2,13):
    for_plot.append(list(sum_of_dice).count(i))
for_plot = np.asarray(for_plot)/sum(for_plot)
xcords= np.linspace(1.5,12.5,11)

fig = plt.figure(figsize=[10,8])
ax = fig.add_axes([0.1,0.1,0.8,0.8])
## density govori gledamo li postotke - y os od 0 do 1, ako True
## stacked govori da se isprinta debug info mislim
## bins - količina podataka - u nasem sl dice ima len 11, tj 2 do 12
ax.hist(sum_of_dice,bins=11,density=True,stacked=True,color="g",orientation="vertical",cumulative=False)
ax.plot(xcords,for_plot,color="r",lw=3,ls="-.")
#dodatna svojstva
# range - pokaži samo dio histograma npr. range=[0,5]
# cumulative - sortira vrijednosti prema kolicini od najmanje do najvece
# histtype= "step" - nema ispune
# orientation=horizontal - očito
# color - očito

fig.show()