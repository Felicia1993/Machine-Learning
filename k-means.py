import matplotlib.pyplot as plot
import seaborn as sns; sns.set()
import numpy as np
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin

def find_cluster(X, n_cluster, rseed = 2):
    nrg = np.random.RandomState(rseed)
    i = nrg.permutation(X.shape[0])[:n_cluster]
    centers = X[i]
    while True:
        labels = pairwise_distances_argmin(X, centers)
        new_centers = np.array([X[labels == i].mean(0) for i in range(n_cluster)])
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels


X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
plot.scatter(X[:,0], X[:, 1], s=50)
# plot.show()

k_means = KMeans(n_clusters=4)
k_means.fit(X)
y_predict = k_means.predict(X)
centers, labels = find_cluster(X, 4)
plot.scatter(X[:,0], X[:,1],c=labels,s=50,cmap='viridis')
plot.scatter(centers[:,0], centers[:,1], c= 'black', s=200, alpha=0.5)
plot.show()







