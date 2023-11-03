import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/'
    'machine-learning-databases/iris/iris.data',
    header=None, encoding='utf-8')

irises = set(df.iloc[:,-1])
print(irises)
counts = {}
for x in irises:
    counts[x] = list(df.iloc[:,-1]).count(x)

print(counts.values())

fig = plt.figure(figsize=(10,8))
ax = fig.add_axes((0.1,0.1,0.9,0.9))
types = tuple(irises)
colors = []
for i in range(len(types)):
    rgb = [np.random.uniform(0,0.5),np.random.uniform(0,0.5),np.random.uniform(0,0.5)]
    colors.append(rgb)

#explode - izvadi dio pie charta definira se lista za svde elemente te se za svaki anvodi kolko
expl = [0]*len(irises)
expl[1] += 0.5
## ok shadow sam radi cool sjenu, autopct piše postotke, textprops - text_properties
text,_,_ = ax.pie(x=tuple(counts.values()),explode=expl,labels=types,colors=colors,shadow=True,autopct="%1.0f%%",
                  textprops={"color":"w","size":20})
print(text)
ax.legend(loc="upper right")
fig.show()
