# Data Mining Project 2: Hierachical Clustering
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal

import pandas as pd
import numpy as np
                
def write_to_excel(clusters, df, file_name):
    output = df[["Public ID", "Gene", "Gene description", "sch9/wt", "ras2/wt", "tor1/wt"]]
    cluster_keys = clusters.keys()
    i = 0
    l = [None] * len(output.index)
    for c in cluster_keys:
        for index in c:
            l[int(index)] = i
        i = i + 1
    output["Clusters"] = l
    #output = output.sort_values(by=['Clusters'])
    #print(output)
    output = output.rename_axis('MyIdx').sort_values(by = ['Clusters', 'MyIdx'])
    output.to_excel(file_name)

def heir(points, num_clusters):
    clusters = dict()
    for i in range(len(points)):
        clusters[i] = points[i]
    while True:
        # Get a list of clusters keys
        k = list(clusters.keys())
        # if length of clusters = num_clusters
        if len(k) == num_clusters:
            # return dict of clusters and new centroids
            # {
            #   [index, index, index, ....]: [x,y,z],
            #   [index, index, index, ....]: [x,y,z],
            #   [index, index, index, ....]: [x,y,z] 
            # }
            final = dict()
            for keys in k:
                p = str(keys)
                p = p.replace('(','')
                p = p.replace(')','')
                p = p.replace(' ', '')
                index = tuple(p.split(','))
                final[index] = clusters[keys]
            return final
        # else
        else: 
            # Get the distance between each point
            dist = dict()
            for i in range(len(k)):
                for j in range(i+1, len(k)):
                    tup = (k[i],k[j])
                    dist[tup] = euclidean_distance(clusters[k[i]], clusters[k[j]])
            # Get the smallest distance
            smallest = min(dist, key=dist.get)
            # Get the new center between the two closest points
            #new_center = find_center(clusters[smallest[0]],clusters[smallest[1]])
            array = np.append([clusters[smallest[0]]], [clusters[smallest[1]]], axis=0)
            new_center = array.mean(axis=0)
            # Add that to the clusters dictionary
            clusters[smallest] = new_center
            # Remove the old indexes from clusters
            del clusters[smallest[0]]
            del clusters[smallest[1]]

# find new center
def find_center(p1,p2):
    l = list()
    for i in range(len(p1)):
        p = (p1[i]+p2[i])/2
        l.append(p)
    a = np.array(l)
    return a

# find distance between points
def euclidean_distance(point1, point2):
    return(sum((point1 - point2) ** 2)) ** 0.5

if __name__ == "__main__":
    df = pd.read_excel("filtered_output.xls")
    # create array from data
    points = df[["sch9/wt", "ras2/wt", "tor1/wt"]].to_numpy()
    # number of desired clusters
    num_clusters = 7

    clusters= heir(points, num_clusters)
    write_to_excel(clusters, df, "filtered_h_7_clusters.xlsx")