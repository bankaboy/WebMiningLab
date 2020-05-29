import math
def euclidian_dist(doc1,doc2):
    dist = 0
    for i in range(9):
        dist += sqrt(doc1[i]**2-doc2[i]**2)
    return dist

def manhattan_dist(doc1,doc2):
    dist = 0
    for i in range(9):
        dist += abs(doc1[i]-doc2[i])
    return dist

def cos_sim(doc1,doc2):
    num, den1, den2 = 0,0,0
    for i in range(7):
        num += doc1[i]*doc2[i]
    for j in range(7):
        den1 += doc1[i]**2
        den2 += doc2[i]**2
    den = den1*den2
    den = math.sqrt(den)
    try:
        sim = num/den
        sim = round(sim,2)
        return sim
    except ZeroDivisionError:
        return 0
        




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

# enter values in dsm 
for i in range(9):
    for j in range(9):
        dsm[i][j] = cos_sim(vsm[i],vsm[j])
        dsm[j][i] = cos_sim(vsm[i],vsm[j])

print("\nDOCUMENT SIMILARITY MATRIX\n")
for i in range(9):
    print(dsm[i])
