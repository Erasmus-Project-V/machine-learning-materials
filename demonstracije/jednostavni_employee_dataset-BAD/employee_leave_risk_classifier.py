import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Perceptron
from sklearn.model_selection import train_test_split
from pldr import plot_decision_regions
from sklearn.preprocessing import StandardScaler, Normalizer

#BAD DATASET

df_employee = pd.read_csv("refinedEmployeeDataset.csv", index_col="ID")
print(df_employee)
X = df_employee.iloc[:, :-1].values
y = df_employee.iloc[:, -1].values
ssc = StandardScaler()
nsc = Normalizer()
X_std = ssc.fit_transform(X)
X_norm = nsc.fit_transform(X)

print(X_std)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, stratify=y, test_size=0.2)

mod_perc = Perceptron()
mod_perc.fit(X_train, y_train)
y_pred = mod_perc.predict(X_test)
correct = 0
yp = list(y_pred)
yt = list(y_test)
corr = 0
for i in range(len(yp)):
    if yp[i] == yt[i]:
        corr += 1

print((corr/len(yp))*100)
print(list(y).count(1),list(y).count(0))
plot_decision_regions(X,y,mod_perc,resolution=0.01)