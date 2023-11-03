import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/'
    'machine-learning-databases/iris/iris.data',
    header=None, encoding='utf-8')


df_sample = df.iloc[-6:,:]
df_sample_arr = df_sample.to_numpy()
columns = ["petal w","petal l" ,"sepal w", "sepal l","label"]
fig = plt.figure(figsize=(10,8))
ax = fig.add_axes((0.1,0.1,0.8,0.8))


##Color template od maptlotliba
ccolors = plt.cm.Blues(np.full(len(columns),0.2))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.box(None)
ax.table(cellText=df_sample_arr,loc="center",colLabels=columns,rowLabels=None,colColours=ccolors)

fig.show()