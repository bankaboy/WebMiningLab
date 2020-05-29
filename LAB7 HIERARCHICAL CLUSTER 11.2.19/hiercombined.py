## Initialisation

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import string
#import math

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

#HIERARCHICAL CLUSTERING

def create_document_matrix(self):
        """Function to create the document distance matrix"""
        self.labels_ = ['doc%d' % (id) for id in self.file_dict]
        main_list = []
        for id1 in self.file_dict:
            temp_list = []
            for id2 in self.file_dict:
                dist = 0
                l1 = 0
                l2 = 0
                for term1, term2 in zip(self.listing_dict_[id1], self.listing_dict_[id2]):
                    l1 += term1**2
                    l2 += term2**2
                    dist += term1 * term2
                dist = dist / (math.sqrt(l1) * math.sqrt(l2))
                temp_list.append(round(math.sqrt(dist), 4))
            main_list.append(temp_list)
            
        self.distance_matrix_ = pd.DataFrame(main_list, index = self.labels_, columns = self.labels_)
        print('\nDistance Matrix')
        print(self.distance_matrix_)
