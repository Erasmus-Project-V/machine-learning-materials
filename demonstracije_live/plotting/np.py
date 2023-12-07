import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



fig, ax = plt.subplots(figsize=[20,8],nrows=1,ncols=3)


x = ["Programer","Matematičar","Pisac","Smetlar","Kuhar"]
y = [20,40,12,43,59]
x_2 = ["Odličan","Vrlo dobar","Dobar","Dovoljan","Nedovoljan"]
y_2 = [30,10,2,43,69]

ax[0].bar(x,y,color="b",width=0.8,edgecolor="k")
ax[0].set_title("Zanimanja ucenika X. gimnazije")


ax[1].bar(x_2,y_2,color="r",width=0.8,edgecolor="k")
ax[1].set_title("Ocjene ucenika X. gimnazije")


df = pd.read_csv("iris.data")
df.columns = ["Sepal_Length","Sepal_Width","PL","PW","class"]

print(df)
df_setosa = df.loc[df["class"] == "Iris-setosa"]
df_virginica = df.loc[df["class"] == "Iris-virginica"]

df_s_x = df_setosa.iloc[:,2].values
df_s_y = df_setosa.iloc[:,3].values

df_v_x = df_virginica.iloc[:,2].values
df_v_y = df_virginica.iloc[:,3].values

ax[2].scatter(df_s_x,df_s_y,color="b",label="setosa")
ax[2].scatter(df_v_x,df_v_y,color="r",label="virginica")
ax[2].set_xlabel("petal width")

ax[2].legend()

from sklearn.linear_model import Perceptron





fig.show()