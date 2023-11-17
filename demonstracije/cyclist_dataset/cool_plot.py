import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("comptagesvelo2015.csv")

fig = plt.figure(figsize=(20,20))

means = df.iloc[:,1:].mean()
print(means)
print(df.columns[1:])
mc = sorted([(means[i],df.columns[i]) for i in range(len(means))])
for i in mc:
    print(i)

rg = np.random
color = [list(rg.uniform(0,1,3)) for i in range(20)]
markers = [".",",","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_",0,1,2,3,4,5,6,7,8,9,10,11]
print(color)

conind = 1
for i in range(1,5):
    for j in range(1,5):
        ax = fig.add_subplot(conind,projection="3d")
        ax.set_title(f"{df.columns[conind]}/{df.columns[conind+1]}")
        ax.scatter(df.iloc[:,i],df.iloc[:,i+1],df.iloc[:,i+2],color=color[i+j],marker=markers[conind-1])
        ax.set_xlim(0,10000)
        ax.set_ylim(0,10000)
        conind += 1



fig.show()

