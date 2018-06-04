from sklearn import ensemble
import pandas as pd
from sklearn.datasets import load_iris, load_boston
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.67)
clf = ensemble.GradientBoostingClassifier(random_state=42)
clf = clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print('Accuracy GradientBoosting Classifier = {0}'.format(accuracy))

boston = load_boston()
X = boston.data
y = boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.67)
regr = ensemble.GradientBoostingRegressor(random_state=42)
regr.fit(X_train, y_train)
accuracy=regr.score(X_test,y_test)
print('Accuracy GradientBoosting Regressor = {0}'.format(accuracy))