## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# VSM PART

doc1 = 'electric automotive motor tesla inc. is likely to introduce its product in india sometime in the summer of 2017'
doc2 = 'automotive major mahindra likely to introduce driverless cars'
doc3 = 'bmw plans to introduce its own motorcycle in india'
doc4 = 'just drive, a self-drive car rental firm uses smart vehicle technology based on iot'
doc5 = 'automotive industry going to hire thousands in 2018'
doc6 = 'famous cricket player dhoni brought his priced car hummer which is an suv'
doc7 = 'dhoni led india to it second world cup victory'
doc8 = 'iot in cars will lead to more safety and make driverless vehicle revolution possible'
doc9 = 'sachin recommended dhoni for indian skipper post' 

k1 = 'automotive'
k2 = 'car'
k3 = 'motorcycles'
k4 = 'self-drive'
k5 = 'iot'
k6 = 'hire'
k7 = 'dhoni'

#initialize vector space matrix 
vsm = [[0 for x in  range(7)]for y in range(9)]

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

terms = []   # Form terms matrix
terms.append(k1)
terms.append(k2)
terms.append(k3)
terms.append(k4)
terms.append(k5)
terms.append(k6)
terms.append(k7)

print('\nDOCUMENT TOKENS\n')   #lists of document tokens
for doc in docs:
    print(doc)

print('\nTERMS TOKENS\n')   #lists of terms tokens
for term in terms:
    print(term)

for i in range(9):      # traverse every document token list
    for j in range(7):    # search for all terms in that document
        if terms[j] in docs[i]:   # if a certain term is found in that document
            vsm[i][j] = docs[i].count(terms[j])   # add the count of the term to the matrix under that document and term indices 
  
print('\nVECTOR SPACE MATRIX\n')  # display vector space matrix
for i in range(9):
    print (vsm[i])

dsm = [[0 for x in  range(9)]for y in range(9)]  #initialize document similarity matrix for similarity between docs

def sim(i,j,matrix):  # fucntion to calculate distances between documents
    dist = 0
    for k in range(7):
        dist+=(matrix[i][k]*matrix[j][k])
    return dist

# enter values in dsm 
for i in range(9):
    for j in range(9):
        dsm[i][j] = sim(i,j,vsm)
        dsm[j][i] = sim(i,j,vsm)

print("\nDOCUMENT SIMILARITY MATRIX\n")
for i in range(9):
    print(dsm[i])

# dictionary for pandas and matplotlib
df = {
    'x': [],
    'y': []
}

# store x and y values of documents in dictionary
for i in range(9):
    for j in range(9):
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


