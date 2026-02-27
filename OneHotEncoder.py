from sklearn.preprocessing import OneHotEncoder

color = [["White"],["Black"],["Yellow"],["Pink"]]

encoder = OneHotEncoder()

result = encoder.fit_transform(color)

print(result.toarray())
