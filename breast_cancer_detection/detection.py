import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Data Preprocessing
dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:, 1:-1]
y = dataset.iloc[:, -1]

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

#Implementing The Model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

#Testing The Model
y_pred = classifier.predict(X_test)
y_pred = np.array(y_pred)
print(np.concatenate(((y_pred.reshape(len(y_pred), 1)), np.array(y_test).reshape(len(np.array(y_test)), 1)), 1))

#Making The Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)