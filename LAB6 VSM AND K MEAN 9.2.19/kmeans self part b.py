## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# VSM PART

f1 = open("partb1.txt",'r')
f2 = open("partb2.txt",'r')
f3 = open("partb3.txt",'r')
f4 = open("partb4.txt",'r')
f5 = open("partb5.txt",'r')
f6 = open("partb6.txt",'r')
f7 = open("partb7.txt",'r')
f8 = open("partb8.txt",'r')
f9 = open("partb9.txt",'r')
f10 = open("partb10.txt",'r')
f11 = open("partb11.txt",'r')
f12 = open("partb12.txt",'r')

k1 = 'Tesla'
k2 = 'electric'
k3 = 'car'
k4 = 'vehicle'
k5 = 'automobile'
k6 = 'pollution'
k7 = 'de-monetisation'
k8 = 'GST'
k9 = 'black money'

#initialize vector space matrix 
vsm = [[0 for x in  range(10)]for y in range(9)]

#get contents of docs
doc1 = f1.read()
doc2 = f2.read()
doc3 = f3.read()
doc4 = f4.read()
doc5 = f5.read()
doc6 = f6.read()
doc7 = f7.read()
doc8 = f8.read()
doc9 = f9.read()
doc10 = f10.read()
doc11 = f11.read()
doc12 = f12.read()


#obtain tokens from documents
doc1 = doc1.split(' ')
doc2 = doc2.split(' ')
doc3 = doc3.split(' ')
doc4 = doc4.split(' ')
doc5 = doc5.split(' ')
doc6 = doc6.split(' ')
doc7 = doc7.split(' ')
doc8 = doc8.split(' ')
doc9 = doc9.split(' ')
doc10 = doc10.split(' ')
doc11 = doc11.split(' ')
doc12 = doc12.split(' ')


docs = []   # Form document matrix
docs.append(doc1)
docs.append(doc2)
docs.append(doc3)
docs.append(doc4)
docs.append(doc5)
docs.append(doc6)
docs.append(doc7)
docs.append(doc8)
docs.append(doc9)
docs.append(doc10)
docs.append(doc11)
docs.append(doc12)


terms = []   # Form terms matrix
terms.append(k1)
terms.append(k2)
terms.append(k3)
terms.append(k4)
terms.append(k5)
terms.append(k6)
terms.append(k7)
terms.append(k8)
terms.append(k9)

print('\nDOCUMENT TOKENS\n')   #lists of document tokens
for doc in docs:
    print(doc)

print('\nTERMS TOKENS\n')   #lists of terms tokens
for term in terms:
    print(term)

for i in range(12):      # traverse every document token list
    for j in range(9):    # search for all terms in that document
        if terms[j] in docs[i]:   # if a certain term is found in that document
            vsm[i][j] = docs[i].count(terms[j])   # add the count of the term to the matrix under that document and term indices 
  
print('\nVECTOR SPACE MATRIX\n')  # display vector space matrix
for i in range(12):
    print (vsm[i])

dsm = [[0 for x in  range(12)]for y in range(12)]  #initialize document similarity matrix for similarity between docs

def sim(i,j,matrix):  # fucntion to calculate distances between documents
    dist = 0
    for k in range(9):
        dist+=(matrix[i][k]*matrix[j][k])
    return dist

# enter values in dsm 
for i in range(12):
    for j in range(12):
        dsm[i][j] = sim(i,j,vsm)
        dsm[j][i] = sim(i,j,vsm)

print("\nDOCUMENT SIMILARITY MATRIX\n")
for i in range(12):
    print(dsm[i])

# dictionary for pandas and matplotlib
df = {
    'x': [],
    'y': []
}

# store x and y values of documents in dictionary
for i in range(12):
    for j in range(12):
        if dsm[i][j]!=0:
            df['x'].append(i)
            df['y'].append(j)

print(df)

# K-MEANS PART

df = pd.DataFrame(df)
print(df)


np.random.seed(200)
k = 3
# centroids[i] = [x, y]
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

## Assignment Stage

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

## Update Stage

import copy

old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k

centroids = update(centroids)
    
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
plt.show()

## Repeat Assigment Stage

df = assignment(df, centroids)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Continue until all assigned categories don't change any more
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()

