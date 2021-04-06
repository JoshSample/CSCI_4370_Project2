# Data Mining Project 2
# # By Makenzie Spurling, Josh Sample, and Kathryn Villarreal
import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum(np.square(point1-point2)))

def init_centroids():
    pass




if __name__ == "__main__":
    # number of clusters
    k = 3
    # number of objects
    n = 0 #obtained from file
    # number of iterations 
    i = 100