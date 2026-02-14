from sklearn.linear_model import LogisticRegression

X = [[30], [40], [50], [70]]
Y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, Y)

print(model.predict([[20]]))
