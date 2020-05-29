f = open("results.txt",'r')

while f.readline():
    entry=f.readline()
    print(entry)

f.close()
