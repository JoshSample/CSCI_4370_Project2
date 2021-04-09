# Data Mining Project 2
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal
import numpy as np
import pandas as pd

sse = 0

# find distance between points
def euclidean_distance(point1, point2):
    total = 0
    for i in range(3):
        total += np.sqrt(np.sum(np.square(point1[i+4]-point2[i+4])))
    return total

# select random centroids based on number of clusters
def init_centroids(k, df):
    return df.sample(n = k)

# method for seeing if there was improvement
def sum_of_squared_errors(k, n, clusteredPoints, centroids):
    sse = 0
    for i in range(k):
        for j in range(n):
            if clusteredPoints[i][j] != 0:
                sse += euclidean_distance(clusteredPoints[i][j], centroids.iloc[i])
    return sse

# clustering algorithm
def kmeans(k, n, iterations, df):
    centroids = init_centroids(k, df)
    # iterate until no more improvement
    for i in range(iterations):
        clusteredPoints = [[0 for x in range(k)] for y in range(n)]
        # assign points to clusters
        for index, row in df.iterrows():
            min = 2
            for j in range(k):
                distance = euclidean_distance(row, centroids.iloc[j])
                if distance < min:
                    min = distance
                    closest = j
            clusteredPoints[closest][index] = row
        sse1 = sse
        sse2 = sum_of_squared_errors(k, n, clusteredPoints, centroids)
        if (sse1 - sse2) / sse1 < 0.0001:
            break
    pass




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