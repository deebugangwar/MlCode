from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,1,0,1,0])

model = LogisticRegression()

kf = KFold(n_splits=5)

scores = cross_val_score(model, X, y, cv=kf)

print(scores)
print("Average Accuracy:", scores.mean())
