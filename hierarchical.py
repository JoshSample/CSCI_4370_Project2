# Data Mining Project 2: Hierachical Clustering
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal

import pandas as pd
import collections

def get_distance(point1, point2):
    # Given two points get the distance between them
    d = []
    for i in range(len(point1)):
        d.append(abs(point1[i] - point2[i]))
    return d

def get_new_center(point1, point2):
    c = []
    for i in range(len(point1)):
        c.append((point1[i] + point2[i])/2)
    return c

def heir(df, num_clusters):
    s = df["sch9/wt"].tolist()
    r = df["ras2/wt"].tolist()
    t = df["tor1/wt"].tolist()
    points = dict()
    # Get all vectors from the three columns
        # Add each vector to a dictionary
    for i in range(len(s)):
        points[i] = [s[i],r[i],t[i]]
    while True:
        # Calculate the distance vector between each vector
        distances = dict()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                k1 = list(points.keys())[i]
                k2 = list(points.keys())[j]
                tup = (k1, k2)
                distances[tup] = get_distance(points[k1],points[k2])
        # Find the smallest distance vector
        sort = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
        # Find the center between those two points
        first_k = list(sort.keys())[0]
        p1 = points[first_k[0]]
        p2 = points[first_k[1]]
        new_point = get_new_center(p1,p2)
        # Add that new center point to the dictionary
        points[first_k] = new_point
        # Remove the two points from before 
        del points[first_k[0]]
        del points[first_k[1]]
        for d in list(distances.keys()):
            if first_k[0] in d:
                del distances[d]
            elif first_k[1] in d:
                del distances[d]

        if len(points) <= int(num_clusters):
            return points
                
def write_to_excel(num_clusters, clusters, df, file_name):
    keys = list(clusters.keys())
    output = df[["sch9/wt", "ras2/wt", "tor1/wt"]]
    l = len(df.index)
    c = [None] * l
    for i in range(int(num_clusters)):
        k = keys[i]
        p = str(k)
        p = p.replace('(','')
        p = p.replace(')','')
        p = p.replace(' ', '')
        index = p.split(',')
        for v in index:
            c[int(v)] = i

    output["Cluster"] = c
    output.to_excel(file_name)

if __name__ == "__main__":
    df = pd.read_excel("filtered_output.xls")
    num_clusters = 3
    clusters = heir(df, num_clusters)
    write_to_excel(num_clusters, clusters, df, "filtered_h_3_clusters.xlsx")