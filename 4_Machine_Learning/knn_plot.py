from mglearn import plot_2d_separator
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=cm.Blues)
plt.xlabel("first feature")
plt.ylabel("second feature")
plot_2d_separator.plot_2d_separator(knn, X)