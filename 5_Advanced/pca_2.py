import numpy as np
pca = PCA()
pca.fit(X)

# lets look at the cumulative explained variance as more components are added:
f, ax = plt.subplots(figsize=(10,5))
ax.plot(np.cumsum(pca.explained_variance_ratio_))
ax.set_xlabel("number of components")
ax.set_ylabel("explained variance ratio")