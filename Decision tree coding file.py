from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
dataset = pd.read_csv('Iris.csv')

#print(dataset.head())
#print(dataset.info())

unique = dataset['Species'].unique()
#print(unique)

label = 0
for i in unique:
    dataset[dataset['Species'] == i] = label
    label += 1

#print(dataset.info())
#print(dataset.tail())

features_X = dataset.iloc[:, : - 1]
#print(features_X.info())

output_Y = dataset.iloc[:, -1]

#print(output_Y.head())

X_train, X_test, Y_train, Y_test = train_test_split(features_X, output_Y, test_size = 0.3, random_state = 1)

dTreeClassifier = tree.DecisionTreeClassifier(criterion = 'gini', random_state = 0)
dTreeClassifier.fit(X_train, Y_train)

output_pred = dTreeClassifier.predict(X_test)

Accuracy = np.mean(output_pred == Y_test) * 100
print(Accuracy)