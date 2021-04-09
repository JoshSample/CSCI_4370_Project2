# Data Mining Project 2
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal
import numpy as np
import pandas as pd
import random

# find distance between points
def euclidean_distance(point1, point2):
    return(sum((point1 - point2) ** 2)) ** 0.5

# assign points by closest centroid
def findClosestCentroids(ic, X):
    assigned_centroid = []
    for i in X:
        distance=[]
        for j in ic:
            distance.append(euclidean_distance(i, j))
        assigned_centroid.append(np.argmin(distance))
    return assigned_centroid

# calculate centroids by finding mean of points 
def calc_centroids(clusters, X):
    new_centroids = []
    new_df = pd.concat([pd.DataFrame(X), pd.DataFrame(clusters, columns=['cluster'])],
                      axis=1)
    for c in set(new_df['cluster']):
        current_cluster = new_df[new_df['cluster'] == c][new_df.columns[:-1]]
        cluster_mean = current_cluster.mean(axis=0)
        new_centroids.append(cluster_mean)
    return new_centroids

# output clustered data to Excel
def output_data(clusters, X):
    new_df = pd.concat([pd.DataFrame(X), pd.DataFrame(clusters, columns=['cluster'])],
                      axis=1)
    new_df.to_excel("kmeans.xls")

# clustering algorithm
def kmeans(k, n, iterations, df):
    # create array from data
    X = df[["sch9/wt", "ras2/wt", "tor1/wt"]].to_numpy()
    # randomly choose centroids
    init_centroids = random.sample(range(0, n), k)
    centroids = []
    for i in init_centroids:
        centroids.append(X[i])
    # iterate until no more improvement
    for i in range(iterations):
        old_centroids = centroids
        # assign the points to a centroid
        get_centroids = findClosestCentroids(centroids, X)
        # calculate new centroids
        centroids = calc_centroids(get_centroids, X)
        # when the centroids don't change, the algorithm has converged
        if np.array_equal(centroids, old_centroids):
            output_data(get_centroids, X)
            break

    
# driver, need dataset, k, and i
if __name__ == "__main__":
    # create dataframe from dataset
    df = pd.read_excel("output.xls")
    # number of clusters
    k = 3
    # number of objects
    n = len(df.index)
    # number of iterations 
    i = 100
    # pass data to algorithm
    kmeans(k, n, i, df)