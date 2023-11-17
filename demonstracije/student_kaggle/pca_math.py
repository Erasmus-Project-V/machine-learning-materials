import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("datasets/math_data_cleaned.csv")


X = df.iloc[:,1:-3].values
y = df.iloc[:,-1].values
print(X)

principal = PCA(n_components=2)
sc = StandardScaler()

X_pca = sc.fit_transform(principal.fit_transform(X))

X_red_inds = np.where(y==8)
X_blue_inds = np.where(y==18)
print(X[X_red_inds])

fig,ax = plt.subplots(figsize=(20,8),nrows=1,ncols=2)

ax[0].scatter(X_pca[X_red_inds][:,0],X_pca[X_red_inds][:,1],color="r")
ax[0].scatter(X_pca[X_blue_inds][:,0],X_pca[X_blue_inds][:,1],color="b")

fig.show()