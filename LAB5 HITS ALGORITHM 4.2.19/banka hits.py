def normalize(scores):
    total = sum(scores)
    for i in range(len(scores)):
        num = scores[i]/total
        scores[i] = num
    return scores

def clear(scores):
    for i in range(len(scores)):
        scores[i] = 0
    return scores

def HITS(G , n):
    hubs, old_hubs = [1 for i in range(n)] , []  # lists containing hubs and authorities scores for each site
    auths, old_auths = [ 0 for i in range(n) ] , []  # intitial values of hubs = 1 , auths = 0 
    stoph = 0.01*n  # to check difference in scores in consecutive iterations 
    stopa = 0.01*n
    counter = 0 
    
    while True:
        old_hubs = hubs    # store previous iteration values for this iteration
        old_auths = auths # not needed for hub score of this iteration but to compare with previous iteration
        
        # for authority score, traverse each column of the matrix
        # wherever 1 is present, find the row number
        # access the hub scores of the sites where 1 is found and add them
        # nomalize the scores,
        # store the value in auth with column subscript
        
        for c in range(n):
            for r in range(n):
                if G[r][c] == 1:  #check if site in column is bieng pointed to buy the site in row
                    auths[c] += old_hubs[r]  # site bieng pointed to is auth and pointing site is hub
        auths = normalize(auths)

        # for hubs score, traverse each row of the matrix
        # wherever 1 is present, find the column number
        # access the hub scores of the sites where 1 is found and add them
        # nomalize the scores,
        # store the value in hub with row subscript

        for r in range(n):
            for c in range(n):
                if G[r][c] == 1:   #check if site in column is bieng pointed to buy the site in row
                    hubs[r] += auths[c]  # site bieng pointed to is auth and pointing site is hub
        hubs = normalize(hubs)

        print("Iteration %d \n" %counter)  # mention iteration number
        
        for i in range(n):  # display hubs and authorities score for that iteration
            print(" %d  -  %d   %d \n" %(i,hubs[i],auths[i]))

        delh = abs(sum(hubs)-sum(old_hubs))   # check for difference in values in 
        dela = abs(sum(auths)-sum(old_auths)) # hubs and authorities scores

        #if delh<stoph and dela<stopa:
        #    break
        #else:
        counter+=1
            

n = int(input("Enter number of websites: "))
G = [[0 for x in range(n)] for y in range(n)]
print("Enter adjecency matrix: ")
for r in range(n):
    for c in range(n):
        print("Enter 1 if %d points to %d: " %(r,c))
        num = int(input())
        G[r][c] = num
print(G)
HITS(G,n)
print("SITE  -  H   A \n")


    


