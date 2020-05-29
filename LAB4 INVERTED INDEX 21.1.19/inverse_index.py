print("DOCUMENTS\n")

docs = []
doc1 = "new home sales top forcast"
doc2 = "home sales rise in july"
doc3 = "increase in home sales in july"
doc4 = "july new homes sales rise"

docs.append(doc1)
docs.append(doc2)
docs.append(doc3)
docs.append(doc4)

word_tokens = []   # list for tokens of (word,doc_id) in first step
doc_freq = []  # list for distinct words and their frequency

# traverse each doc, and create token list of the word and the docID
i = 0
for doc in docs:
    words = doc.split()
    for word in words:
        word_tokens.append([word,i+1])
        doc_freq.append(word)
    i+=1
    print(doc)

# print the term tokens (term,docID) collected from the docs
print('\nTHE WORD TOKENS COLLECTED FROM THE DOCUMENTS')
print('\nTERM:DOC ID')
for token in word_tokens:
    print(token)

# print the distinct words and their frequencies (term,doc_freq)
print('\nWORDS AND THEIR DOCUMENT FREQUENCY')
print('\nTERM:DOC FREQ')

# make a list of only distinct words
doc_freq_distinct_terms = list(set(doc_freq))

# for each distinct word in the distinct list
# search for its frequency in the list containing
# all the words (repeated)
for word in doc_freq_distinct_terms:
    print(str(word)+":"+str(doc_freq.count(word)))

posting_list = {} # dictionary for containing the postings lists for each term

# for each distinct word in the overall documents,
# store it in a dictionary with empty list as value
# initialisation for postings_lists data
for word in doc_freq_distinct_terms:
    posting_list[word] = []

# for each distinct word, search each document individually.
# if the word is present in the document, append the document id
# to the value of the word_key in the posting_list dictionary
for i in range(4):
    doc = docs[i]
    doc = doc.split()
    for word in doc_freq_distinct_terms:
        if word in doc:
            posting_list[word].append(i+1)

print('\nWORDS AND THEIR POSTING LISTS')
print('\nTERM:POSTING LIST')

for entry in posting_list:
    print(str(entry)+":"+str(posting_list[entry]))

