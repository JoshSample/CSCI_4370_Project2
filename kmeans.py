# Data Mining Project 2
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal
import numpy as np
import pandas as pd

# find distance between points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum(np.square(point1-point2)))

# select random centroids based on number of clusters
def init_centroids(k, df):
    return df.sample(n = k)

# method for seeing if there was improvement
def sum_of_squared_errors():
    pass

# clustering algorithm
def kmeans(k, n, iterations, df):
    centroids = init_centroids(k, df)
    
    # iterate until no more improvement
    for i in range(iterations):
        # assign points to clusters
        for j in range(n):




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