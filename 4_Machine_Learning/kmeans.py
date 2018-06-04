
f, ax = plt.subplots(1,3, figsize=(20,5))
ax[0].scatter(X_iris[:,0], X_iris[:,1], c=y_iris)
ax[0].set_title("ground truth")
ax[1].scatter(X_iris[:,0], X_iris[:,1], c=k_means.labels_)
ax[1].set_title("kmeans: 2 components")

k_means = cluster.KMeans(n_clusters=4)
k_means.fit(X_iris)

ax[2].scatter(X_iris[:,0], X_iris[:,1], c=k_means.labels_)
ax[2].set_title("kmeans: 3 components")