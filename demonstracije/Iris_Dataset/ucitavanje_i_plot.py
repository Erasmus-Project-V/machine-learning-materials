import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/'
    'machine-learning-databases/iris/iris.data',
    header=None, encoding='utf-8')

df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
print(df.columns)
classes = list(set(df["class"]))


# df.loc je vrlo powerful utility
class1 = df.loc[df["class"] == classes[0]].iloc[:, ].values
class2 = df.loc[df["class"] == classes[1]].iloc[:, ].values
class3 = df.loc[df["class"] == classes[2]].iloc[:, ].values
print(class1)

fig, ax = plt.subplots(figsize=(15, 8), nrows=1, ncols=2)


ax[0].set_title("Iris dataset")
ax[0].set_xlabel("Sepal length")
ax[0].set_ylabel("Sepal width")
ax[1].set_title("Iris dataset")
ax[1].set_xlabel("Petal length")
ax[1].set_ylabel("Petal width")
for i in range(2):
    el1 = ax[i].scatter(class1[:, 2 * i], class1[:, 2 * i + 1], s=10, c="b", label=classes[0])
    el2 = ax[i].scatter(class2[:, 2 * i], class2[:, 2 * i + 1], s=10, c="r", label=classes[1])
    el3 = ax[i].scatter(class3[:, 2 * i], class3[:, 2 * i + 1], s=10, c="y", label=classes[2])
    ax[i].legend(handles=(el1, el2, el3))
fig.show()
