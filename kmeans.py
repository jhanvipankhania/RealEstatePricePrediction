
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#Creating random array element to store data values(resembles the data set)

Y = np.array([[1 ,4], [1.6, 2, 9], [6,9], [8,9], [1,1.04], [10,12]])

plt.scatter(Y[:,0], Y[:,1], s = 160)
plt.show()

colors = 10*["g", "r", "c", "b", "k"]


class K_means:
    def __init__(self, k=2, tol = 0.001, max_iter = 300):
        sefl.k = k
        self.tol=tol
        self.max_iter = max_iter
    def fir(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

        for i in range(self.k):
            self.classifications[i] = []

        for featureset in data:
            distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(featureset)
            prev_centroids = dict(self.centroids)

        for classification in self.classifications:
            self.centroids[classification] = np.average(self.classifications[classification], axis = 0)
