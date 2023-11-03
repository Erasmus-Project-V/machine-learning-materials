import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

from ubacivanje_u_modele import default_load
from custom_built_model import AdalineSGD
from sklearn.preprocessing import StandardScaler as ssc1
from plot_decision_regions import plotScatter, plot_losses


class StandardScaler:

    def fit(self, X_0):
        self.svl = []
        for i in range(X_0.shape[1]):
            self.svl.append({"mean": X_0[:, i].mean(), "std": X_0[:, i].std()})

    def transform(self, X_0):
        X_0 = X_0.copy()
        assert X_0.shape[1] == len(self.svl)
        for i in range(X_0.shape[1]):
            X_0[:, i] = (X_0[:, i] - self.svl[i]["mean"]) / self.svl[i]["std"]
        return X_0

    def fit_transform(self, X_0):
        self.fit(X_0)
        return self.transform(X_0)


def standardize(training_dataset):
    X_0 = np.copy(training_dataset)
    training_dataset[:, 0] = (X_0[:, 0] - X_0[:, 0].mean()) / X_0[:, 0].std()
    training_dataset[:, 1] = (X_0[:, 1] - X_0[:, 1].mean()) / X_0[:, 1].std()
    return X_0


df, ced = default_load(no_classes=2)
X = df.iloc[:, 2:4].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True, test_size=0.5)
sc = StandardScaler()
sc2 = ssc1()
X_train_std_1 = sc.fit_transform(X_train)
X_train_std_2 = sc2.fit_transform(X_train)


def PlotSSC():
    fig, ax = plt.subplots(figsize=(20, 8), nrows=1, ncols=2)
    ax[0].scatter(X_train_std_1[:, 0], X_train_std_1[:, 1], marker="o", c="r")
    ax[0].set_title("Custom stdsc")
    ax[1].scatter(X_train_std_2[:, 0], X_train_std_2[:, 1], marker="o", c="b")
    ax[1].set_title("Sklearn stdsc")

    fig.show()


# PlotSSC()


class ModelSupp:

    def __init__(self, mod, sc):
        self.model = mod
        self.sc = sc

    def predict(self, X):
        X_std = sc.transform(X)
        pred = self.model.predict(X_std)
        return pred


model = AdalineSGD(eta=0.001, n_iter=100)
model.fit(X_train_std_1, y_train)
mp = ModelSupp(model, sc)
preds = mp.predict(X_test)
no_acc = (y_test == preds).sum()
fig, axes = plt.subplots(figsize=(20, 8), nrows=1, ncols=2)
plotScatter(X, y, mp, 0.15, axes[0])
print(no_acc / len(y_test))
plot_losses(model.losses_, axes[1])
fig.show()
