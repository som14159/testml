import pandas as pd
import random
from collections import defaultdict


df = pd.read_csv('data_class.csv')

print(df)

x = int(input("x :"))
y = int(input("y :"))
k = int(input("k :"))

def distance_bw(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

values = []
    
for i in df.values:
    d = distance_bw([i[0],i[1]],[x,y])
    values.append([d,i[2],i[0],i[1]])

values = sorted(values)

votes = defaultdict(int)

for i in range(k):
    
    print(values[i][2],",",values[i][3],'->',values[i][1])
    votes[values[i][1]] += 1

maxCount = 0

for category,count in votes.items():
    if count > maxCount:
        prediction = category
        maxCount = count

print(prediction)

