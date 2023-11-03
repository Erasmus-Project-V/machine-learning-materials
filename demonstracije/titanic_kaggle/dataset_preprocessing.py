import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from mpl_toolkits import mplot3d

df = pd.read_csv("dataset/train.csv")

print(df.columns)

print(df.iloc[:3, :])

# micanje aplsolutno beskorisnih vrijednosti
df_useless_data = df[["Name", "Ticket", "Cabin"]]
# Iako cabin nije u potpunosti beskorisna - novonastali vektor nakon OHE bi bio prekompleksan
for i in df_useless_data.columns:
    del df[i]

print(df)

for i in df.columns:
    print(f"values present in {i}: {set(df[i])}")
# values za spol će biti zamijenjene binarnim vrijednostima female:1 ili 0
df["Sex"] = df["Sex"].map(lambda a: {"male": 0, "female": 1}[a])
cls = list(df.columns)
cls[3] = "Female"
df.columns = cls
print(df["Female"])

# values za embarked će biti one_hot enkodirane koristeci pd.get_dummies
print("Number of unknown Embarkments:", list(df["Embarked"]).count(np.nan))
# postoje samo 2 unknowna, stoga ću ih fillati sa random embarked value
df["Embarked"] = df["Embarked"].fillna(value="S")

## OneHotEncodeat ću embarked values
df = df.join(pd.get_dummies(df["Embarked"], prefix="Embarked", prefix_sep="_", dtype=int))
del df["Embarked"]
df = df.fillna(df.mean())

for i in df.columns:
    print(f"values present in {i}: {set(df[i])}")

##Sada je dataset preprocessed, te se može napraviti nekolicina koristnih plotova
##dodatno, spremiti ću daaset za korištenje pri modeliranju

df.to_csv("dataset/titanic_processed.csv",index=False)


fig, ax = plt.subplots(figsize=(26, 8), nrows=1, ncols=4)

ax[0].set_title("survival by gender ratio")
all_passengers = df[["Survived", "Female"]]
males = all_passengers.loc[all_passengers["Female"] == 0].values
females = all_passengers.loc[all_passengers["Female"] == 1].values
s_m = (males[:, 0] == 1).sum()
s_f = (females[:, 0] == 1).sum()
d_m = males.shape[0] - s_m
d_f = females.shape[0] - s_f
print(s_m, d_m, s_f, d_f)
ax[0].set_xlim(-0.5, 1.5)
ax[0].bar(("Survived", "Died"), (s_m, d_m), width=0.4, color="b", edgecolor="k", label="male")
ax[0].bar(("Survived", "Died"), (s_f, d_f), width=0.4, color="r", bottom=(s_m, d_m), edgecolor="k", label="female")
ax[0].legend(loc="upper left")

##potencijalno dodati survival_by_class??? i još koji parametar?


# age and fare scatterplot

sagf = df[["Age", "Fare","Female", "Survived"]]
saf_surv = sagf.loc[sagf["Survived"] == 1]
saf_dead = sagf.loc[sagf["Survived"] == 0]
print(sagf)
ax[1].set_title("People by age and fare")
ax[1].set_xlabel("age/years")
ax[1].set_ylabel("fare/kn")
ax[1].scatter(saf_dead.values[:, 0], saf_dead.values[:, 1], marker="o", color="b", label="died")
ax[1].scatter(saf_surv.values[:, 0], saf_surv.values[:, 1], marker="o", color="r", label="survived")
ax[1].legend(loc="upper right")

ax[2].set_title("survival by class")
cl = "Pclass"
sc = df[[cl, "Survived"]]
survived_c = []
dead_c = []
for i in range(3):
    class_x = all_passengers.loc[sc[cl] == i + 1].values
    s_cx = (class_x[:, 1] == 1).sum()
    d_cx = class_x.shape[0] - s_cx
    survived_c.append(s_cx)
    dead_c.append(d_cx)
ax[2].set_xlim(-0.5, 1.5)
print(survived_c, dead_c)
ax[2].bar(("Survived", "Died"), (survived_c[0], dead_c[0]), width=0.4, color="b", edgecolor="k", label="male")
colors = ("r", "y")
for i in range(2):
    ax[2].bar(("Survived", "Died"), (survived_c[i], dead_c[i]), bottom=(survived_c[i - 1], dead_c[i - 1]), width=0.4,
              color=colors[i], edgecolor="k", label="male")

ax3 = fig.add_subplot(anchor="E",projection="3d")
ax3.scatter3D(saf_surv.values[:, 0], saf_surv.values[:, 1],saf_surv.values[:,2], marker="o",alpha=0.5, color="b", label="survived")
ax3.scatter3D(saf_dead.values[:, 0], saf_dead.values[:, 1],saf_dead.values[:,2], marker="x", color="r", label="died")

ax3.legend(loc="upper right")
ax3.set_xlabel("Age")
ax3.set_ylabel("Fare/kn")
ax3.set_zlabel("Female")

fig.show()

