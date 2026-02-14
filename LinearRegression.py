from sklearn.linear_model import LinearRegression
marks = [[20], [30], [99]]
hours = [1, 2, 3]

model = LinearRegression()
model.fit(marks, hours)

next_hours = model.predict([[100]])
print(next_hours)
