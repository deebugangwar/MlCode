from sklearn.cluster import KMeans

X = [[30], [40], [50], [70]]

model = KMeans(n_clusters=2, random_state=0)
model.fit(X)

print(model.labels_)
