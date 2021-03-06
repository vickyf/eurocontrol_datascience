from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.67)

clf = tree.DecisionTreeClassifier(random_state=42)
clf = clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print('Accuracy tree = {0}'.format(accuracy))