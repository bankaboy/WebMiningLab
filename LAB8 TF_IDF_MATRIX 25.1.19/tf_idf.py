import math

df, idf = [0 for i in range(7)], [0 for i in range(7)] #store values of tf and idf for each term
tf_idf = [[0 for x in range(7)] for y in range(9)] #initialize tf_idf matrix
terms = []   # Form terms matrix
docs = []   # Form document matrix
#initialize vector space matrix 
vsm = [[0 for x in  range(7)]for y in range(9)]

#FUNCTIONS

def form_vsm(docs,terms):
    rows = len(docs)
    cols = len(terms)
    for i in range(rows):      # traverse every document token list
        for j in range(cols):    # search for all terms in that document
            if terms[j] in docs[i]:   # if a certain term is found in that document
                vsm[i][j] = docs[i].count(terms[j])   # add the count of the term to the matrix under that document and term indices 

def print_each(list_given):   
    for single in list_given:
        print(single)

def inv_doc_freq(df,docs):
    for i in range(7):       
        den = df[i]
        num = len(docs)
        try:
            a = num/den
            print(a)
        except ZeroDivisionError:
            a = 1
        idf[i] = math.log(a,10)

def calc_df(df,vsm,docs,terms):
    cols = len(terms)
    rows = len(docs)
    for c in range(cols):           
        for r in range(rows):
            df[cols] += vsm[rows][cols]

def calc_tf_idf(docs,terms,vsm,tf_idf):
    cols = len(terms)
    rows = len(docs)
    for r in range(rows):               
        for c in range(cols):
            tf_idf[r][c] = round(vsm[r][c]*idf[c],2)

def max_key_assign(docs,tf_idf,terms):
    rows = len(docs)
    for i in range(9):
        max_key = max(tf_idf[i])
        index = tf_idf[i].index(max_key)
        key = terms[index]
        print(" Document %d : Best Keyword %s \n" %(i,key))
    
    

# DOCUMENTS

doc1 = 'electric automotive motor tesla inc. is likely to introduce its product in india sometime in the summer of 2017'
doc2 = 'automotive major mahindra likely to introduce driverless cars'
doc3 = 'bmw plans to introduce its own motorcycle in india'
doc4 = 'just drive, a self-drive car rental firm uses smart vehicle technology based on iot'
doc5 = 'automotive industry going to hire thousands in 2018'
doc6 = 'famous cricket player dhoni brought his priced car hummer which is an suv'
doc7 = 'dhoni led india to it second world cup victory'
doc8 = 'iot in cars will lead to more safety and make driverless vehicle revolution possible'
doc9 = 'sachin recommended dhoni for indian skipper post' 

#KEYWORDS

k1 = 'automotive'
k2 = 'car'
k3 = 'motorcycles'
k4 = 'self-drive'
k5 = 'iot'
k6 = 'hire'
k7 = 'dhoni'

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

docs.append(doc1)
docs.append(doc2)
docs.append(doc3)
docs.append(doc4)
docs.append(doc5)
docs.append(doc6)
docs.append(doc7)
docs.append(doc8)
docs.append(doc9)

terms.append(k1)
terms.append(k2)
terms.append(k3)
terms.append(k4)
terms.append(k5)
terms.append(k6)
terms.append(k7)

#lists of document tokens
print('\nDOCUMENT TOKENS\n')   
print_each(docs)

#lists of terms tokens
print('\nTERMS TOKENS\n')   
print_each(terms)

#print term frequency 
form_vsm(docs,terms)

# display vector space matrix
print_each(vsm)


#calculate document frequency of each term
calc_df(df,vsm,docs,terms)
   

# display term frequencies
print('\nDOCUMENT FREQUENCIES\n') 
print_each(df)

# display inverse document frequencies
inv_doc_freq(df,docs)
print('\nINVERSE DOCUMENT FREQUENCIES\n')  
print_each(idf)

#calculate tf idf matrix
calc_tf_idf(docs,terms,vsm,tf_idf)

# display vector space matrix
print_each(tf_idf)


#finding most appropriate keyword for each document
print('\nMAX KEY FOR EACH DOCUMENT\n')  
max_key_assign(docs,tf_idf,terms)

          
