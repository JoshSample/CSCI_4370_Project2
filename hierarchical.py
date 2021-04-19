# Kathryn Villarreal
# Heirarchial Clustering

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
    points1 = dict()
    points2 = dict()
    points3 = dict()
    points4 = dict()
    # Get all vectors from the three columns
        # Add each vector to a dictionary
    for i in range(0,len(s)-3,4):
        points1[i] = [s[i],r[i],t[i]]
        points2[i+1] = [s[i+1],r[i+1],t[i+1]]
        points3[i+2] = [s[i+2],r[i+2],t[i+2]]
        points4[i+3] = [s[i+3],r[i+3],t[i+3]]
        if (i+4)>(len(s)-3):
            points1[i+4] = [s[i+4],r[i+4],t[i+4]]
            points2[i+5] = [s[i+5],r[i+5],t[i+5]]
    # Loop
    distances1 = dict()
    distances2 = dict()
    distances3 = dict()
    distances4 = dict()
    once = False
    while True:
        # Calculate the distance vector between each vector
        #distances = dict()
        for i in range(len(points1)):
            for j in range(i+1, len(points1)):
                k11 = list(points1.keys())[i]
                k12 = list(points1.keys())[j]
                k21 = list(points2.keys())[i]
                k22 = list(points2.keys())[j]
                try:
                    k31 = list(points3.keys())[i]
                    k32 = list(points3.keys())[j]
                    k41 = list(points4.keys())[i]
                    k42 = list(points4.keys())[j]
                except:
                    k31 = None
                tup1 = (k11,k12)
                tup2 = (k21,k22)
                tup3 = tuple()
                tup4 = tuple()
                if k31 != None:
                    tup3 = (k31,k32)
                    tup4 = (k41,k42)
                if once == False:
                    distances1[tup1] = get_distance(points1[k11],points1[k12])
                    distances2[tup2] = get_distance(points2[k21],points2[k22])
                    if k31 != None:
                        distances3[tup3] = get_distance(points3[k31],points3[k32])
                        distances4[tup4] = get_distance(points4[k41],points4[k42])
                elif tup1 not in list(distances1.keys()):
                    distances1[tup1] = get_distance(points1[k11],points1[k12])
                elif tup2 not in list(distances2.keys()):
                    distances2[tup2] = get_distance(points2[k21],points2[k22])
                elif k31 != None:
                    if tup3 not in list(distances3.keys()):
                        distances3[tup3] = get_distance(points3[k31],points3[k32])
                    if tup4 not in list(distances4.keys()):
                        distances4[tup4] = get_distance(points4[k41],points4[k42])
        # Find the smallest distance vector
        sort1 = {k: v for k, v in sorted(distances1.items(), key=lambda item: item[1])}
        sort2 = {k: v for k, v in sorted(distances2.items(), key=lambda item: item[1])}
        sort3 = {k: v for k, v in sorted(distances3.items(), key=lambda item: item[1])}
        sort4 = {k: v for k, v in sorted(distances4.items(), key=lambda item: item[1])}
        # Find the center between those two points
        first_k = list(sort1.keys())[0]
        p1 = points1[first_k[0]]
        p2 = points1[first_k[1]]
        new_point = get_new_center(p1,p2)
        # Add that new center point to the dictionary
        points1[first_k] = new_point
        # Remove the two points from before 
        del points1[first_k[0]]
        del points1[first_k[1]]
        for d in list(distances1.keys()):
            if first_k[0] in d:
                del distances1[d]
            elif first_k[1] in d:
                del distances1[d]
        
        # Find the center between those two points
        first_k = list(sort2.keys())[0]
        p1 = points2[first_k[0]]
        p2 = points2[first_k[1]]
        new_point = get_new_center(p1,p2)
        # Add that new center point to the dictionary
        points2[first_k] = new_point
        # Remove the two points from before 
        del points2[first_k[0]]
        del points2[first_k[1]]
        for d in list(distances2.keys()):
            if first_k[0] in d:
                del distances2[d]
            elif first_k[1] in d:
                del distances2[d]
        
        # Find the center between those two points
        first_k = list(sort3.keys())[0]
        p1 = points3[first_k[0]]
        p2 = points3[first_k[1]]
        new_point = get_new_center(p1,p2)
        # Add that new center point to the dictionary
        points3[first_k] = new_point
        # Remove the two points from before 
        del points3[first_k[0]]
        del points3[first_k[1]]
        for d in list(distances3.keys()):
            if first_k[0] in d:
                del distances3[d]
            elif first_k[1] in d:
                del distances3[d]

        # Find the center between those two points
        first_k = list(sort4.keys())[0]
        p1 = points4[first_k[0]]
        p2 = points4[first_k[1]]
        new_point = get_new_center(p1,p2)
        # Add that new center point to the dictionary
        points4[first_k] = new_point
        # Remove the two points from before 
        del points4[first_k[0]]
        del points4[first_k[1]]
        for d in list(distances4.keys()):
            if first_k[0] in d:
                del distances4[d]
            elif first_k[1] in d:
                del distances4[d]

        if len(points1) <= int(num_clusters):
            points = {**points1, **points2, **points3, **points4}
            distances = dict()
            while True:
                # Calculate the distance vector between each vector
                #distances = dict()
                for i in range(len(points)):
                    for j in range(i+1, len(points)):
                        k1 = list(points.keys())[i]
                        k2 = list(points.keys())[j]
                        tup = (k1,k2)
                        if tup not in list(distances1.keys()):
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
    once = True
                
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
    df = pd.read_excel("output.xls")
    num_clusters = input("How many clusters would you like?  ")
    clusters = heir(df, num_clusters)
    print(clusters)
    write_to_excel(num_clusters, clusters, df, "h_3_clusters.xlsx")