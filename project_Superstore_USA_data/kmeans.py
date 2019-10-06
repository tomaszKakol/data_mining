# source https://www.michael-grogan.com/k-means-clustering-python-sklearn/
import pandas as pd
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


df = pd.read_excel('Superstore.xls')

_xName = 'Discount'
_yName = 'Profit'
# Quantity / Sales

X = df[[_xName]]
Y = df[[_yName]]

pl.plot(X, Y, '*')
pl.xlabel(_xName)
pl.ylabel(_yName)
pl.title('Real data')
pl.show()

X_norm = (X - X.mean()) / (X.max() - X.min())
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())
pl.scatter(Y_norm, X_norm)
pl.xlabel(_xName)
pl.ylabel(_yName)
pl.title('Data normalization')
pl.show()

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
# print(kmeans)
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
# print(score)
pl.plot(Nc, score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()

pca = PCA(n_components=1).fit(Y_norm)
pca_d = pca.transform(Y_norm)
pca_c = pca.transform(X_norm)

kmeans = KMeans(n_clusters=3)
kmeansoutput = kmeans.fit(Y_norm)
# print(kmeansoutput)
pl.figure('3 Cluster K-Means')
pl.scatter(pca_d[:, 0], pca_c[:, 0], c=kmeansoutput.labels_)
labels = kmeansoutput.labels_
# print(labels)
pl.xlabel(_xName)
pl.ylabel(_yName)
pl.title('3 Cluster K-Means')
pl.show()


