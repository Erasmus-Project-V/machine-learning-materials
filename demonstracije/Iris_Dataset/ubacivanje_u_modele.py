import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler, Normalizer
from plot_decision_regions import plotScatter


def default_load(no_classes=3):
    df = pd.read_csv(
        'https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data',
        header=None, encoding='utf-8').iloc[:50 * no_classes, :]

    df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

    LE = LabelEncoder()
    df["class"] = pd.DataFrame(LE.fit_transform(df["class"].values))
    classes_enc_dict = {list(LE.classes_)[i]: i for i in range(len(list(LE.classes_)))}
    return df, classes_enc_dict


def main():
    df, classes_enc_dict = default_load()
    standardizer = StandardScaler()
    normalizer = Normalizer()
    model_perceptron_no_sgd = Perceptron()
    model_lr = LogisticRegression(solver="liblinear", penalty="l2", C=1.0)
    model_dt = DecisionTreeClassifier(criterion="gini")
    model_df = RandomForestClassifier(n_estimators=100)
    model_svm = SVC(kernel="linear")

    X = df.iloc[:, 2:4].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True, test_size=0.1)

    pipeline = Pipeline([("std_01", standardizer), ("model", model_df)])
    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    print(preds)
    print(y_test)
    # ovo neće biti bool već np array
    no_acc = (y_test == preds).sum()
    total = len(y_test)
    print(no_acc, total)
    print(f"total accuracy: {no_acc * 100 / total}%")

    fig, axes = plt.subplots(figsize=(20, 8), nrows=1, ncols=2)

    plotScatter(X, y, pipeline, 0.15, axes[0])
    ms = pipeline["model"]

    fig.show()


if __name__ == "__main__":
    main()
