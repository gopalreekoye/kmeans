#reekoye gopal
#rkygop001

#ML assignment 1- K-Mean clutering


import numpy as np


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(((x1[0]-x2[0])**2)+((x1[1]-x2[1])**2))

    
class Kmeans:
    def __init__(self, K=3, max_iters=20):
        self.K = K
        self.max_iters = max_iters

        #list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]

        #mean example number for each cluster
        self.centroids = []

    def predict(self, X):
        self.X = X
        self.n_samples = 8
        self.n_features = 2

        #initialise the centroids
        self.centroids = [[2,10],[5,8],[1,2]]

        #optimization
        for _ in range (self.max_iters):
            #update clusters
            self.clusters = self.create_clusters(self.centroids)
            
            #update centroids
            centroids_old - self.centroids
            self.centroids = self.get_centroids(self.clusters)

            #check for convergence
            if self.is_converged(centroids_old, self.centroids):
                break

        #print something
        print("Success!")



    def create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for x in range(8):
            centroid_idx = self.closest_centroid(X[x], centroids)
            clusters[centroids_idx].append(X[x])
        return clusters

    def closest_centroids(self, sample, centroids):
        distance = [euclidean_distance(sample,self.X[point-1])for point in centroids]
        closest_idx = np.argmin(distances)
        return closest_idx

    def get_centroids(self, clusters):
        centroids = np.zeros((3, 2))
        for idx in (3):
            cluster_mean = np.mean (clusters[idx], axis=0)
            centroids[idx] = cluster_mean
        return centroids

    def is_converged(self, centroids_old, centroids):
        distances=[euclidean_distance(centroids_old[i], centroids[i]) for i in(3)]
        return sum(distances) == 0


