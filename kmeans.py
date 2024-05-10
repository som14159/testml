import pandas as pd
import random
from collections import defaultdict
import numpy as np
df = pd.read_csv('data.csv')

print(df)

no_of_clusters = int(input("Enter No of Clusters:"))

centroid = random.sample(df.values.tolist(),no_of_clusters)


def distance_bw(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

print("Initital Centroid")
print(centroid)

while True:
    
    old_centroid = centroid.copy()
    clusters = defaultdict(list)

    for i in df.values:
        closest = -1
        min_distance = 1e7
        for j in range(len(centroid)):
            d = distance_bw(i,centroid[j])
            if d < min_distance:
                min_distance = d
                closest = j
        clusters[closest].append(i)

    centroid = []
    for c,points in clusters.items():
        centroid.append([np.mean(points[:][0]),np.mean(points[:][1])])
        
    print("New Centroid:")
    print(centroid)
    if centroid == old_centroid:
        for c,points in clusters.items():
            print(f"Cluster {c}:")
            for i in points:
                print("\t",i)
        break

