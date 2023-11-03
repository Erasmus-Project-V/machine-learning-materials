import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron, LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dataset/titanic_processed.csv")

print(df.iloc[1, :])
X = df.iloc[:, 2:].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True, test_size=0.2)


def asses_f_i():
    feat_labels = df.columns[2:]
    forest = RandomForestClassifier(n_estimators=500, random_state=1)
    forest.fit(X_train, y_train)
    importance = forest.feature_importances_

    indices = np.argsort(importance)[::-1]
    plt.title('Feature importance')
    plt.bar(range(X_train.shape[1]),
            importance[indices],
            align='center', edgecolor="k")
    plt.xticks(range(X_train.shape[1]),
               feat_labels[indices], rotation=90)
    plt.xlim([-1, X_train.shape[1]])
    plt.tight_layout()
    plt.show()
    # najvažniji features su upravo female, age i fare, kao što se moglo i vidjeti u vizualnoj analizi


# asses_f_i()

X_important = df[["Female", "Age", "Fare"]].values

models = {"perceptron": Perceptron(),
          "logr": LogisticRegression(C=1),
          "svm": SVC(),
          "decision tree": DecisionTreeClassifier(),
          "random forest": RandomForestClassifier(n_estimators=100)}

from sklearn.model_selection import StratifiedKFold

sc = StandardScaler()
X_important_std = sc.fit_transform(X_important)

X_train, X_test, y_train, y_test = train_test_split(X_important, y, stratify=y, shuffle=True, test_size=0.2)
X_train_std, X_test_std, y_train_std, y_test_std = train_test_split(X_important_std, y, stratify=y, shuffle=True, test_size=0.2)

kf = StratifiedKFold(n_splits=10)


avg_tt = {}
avg_tt_std = {}
import time
results = {}
results_std = {}
for mod in models.items():
    rloc = []
    rloc_std = []
    tloc = []
    tloc_std = []
    for i, (train, test) in enumerate(kf.split(X_train,y_train)):
        t0 = time.perf_counter()
        mod[1].fit(X_train_std[train], y_train_std[train])
        score_std = mod[1].score(X_train[test], y_train[test])
        t1 = time.perf_counter()-t0
        tloc.append(t1)
        t0_std = time.perf_counter()
        mod[1].fit(X_train[train], y_train[train])
        score = mod[1].score(X_train[test], y_train[test])
        t_1_std = time.perf_counter()-t0_std
        tloc_std.append(t_1_std)
        rloc.append(score)
        rloc_std.append(score_std)
        print(f"fold {i}; accuracy: {score}, accuracy_standardized: {score_std}")
    print(f"model {mod[0]}, mean accuracy {np.asarray(rloc).mean()*100}% \n"
          f"standardized accuracy: {np.asarray(rloc_std).mean()*100}%")
    results[mod[0]] = np.asarray(rloc).mean()
    results_std[mod[0]] = np.asarray(rloc_std).mean()
    avg_tt[mod[0]] = np.asarray(tloc).mean()
    avg_tt_std[mod[0]] = np.asarray(tloc_std).mean()

fig,ax = plt.subplots(figsize=(20,8),ncols=3,nrows=1)
ax[0].set_title("average model accuracy")
ax[0].set_ylim((0,1))
ax[0].bar(results.keys(),np.asarray(list(results.values())).round(3),color="g",edgecolor="k",)
## ovaj dataset se ne može odvojiti standardizacijom!

ax[1].set_title("average std model accuracy")
ax[1].bar(results_std.keys(),np.asarray(list(results_std.values())).round(3),color="r",edgecolor="k",)
ax[1].set_ylim(ax[0].get_ylim())


ax[2].set_title(f"average training time by model/miliseconds \n"
                f"per 100 examples")
print(100/71)
spacing = np.arange(0,5,1)
print(spacing)
ax[2].bar(spacing,np.asarray(list(avg_tt.values())).round(4)*1000*(100/71),color="b",edgecolor="k",width=0.5,label="normal")
ax[2].bar(spacing+0.5,np.asarray(list(avg_tt_std.values())).round(4)*1000*(100/71),color="y",edgecolor="k",width=0.5,label="std")
ax[2].set_xticks(spacing+0.5/2,avg_tt.keys())
ax[2].legend(loc="upper left")


fig.show()
