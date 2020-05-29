def ranker():
    
    d = 0.5 #default taken
    n = int(input('Enter number of sites: ')) # number of sites
    netGraph = [[0 for x in range(n)] for y in range(n)] #initialise graph
    PR = [ 1 for x in range(n)] #initially all page ranks =1
    numOut = [] #number of outgoing sites for each site
    
    for i in range(0,n):
        for j in range(0,n):
            print('Enter 1 if site '+str(i)+' directs to site '+str(j))
            num = int(input())
            netGraph[i][j] = num

    print('The Network Graph is : \n')
    for x in netGraph:
        print(*x, sep=" ")

    for i in netGraph:
        numOut.append(i.count(1)) # store number of outgoing sites

    print('\nThe number of outgoing sites for each site is\n')
    for num in range(n):
        print('Site '+str(num)+' : '+str(numOut[num]))

    print('\n')
    for iteration in range(n):
        for site in range(n):
            subject = netGraph[iteration][site]
            if netGraph[iteration][site] == 1:
                PR[subject] = (1-d)+d*(PR[site]/numOut[site])
        print(PR)
        
    print('\n The rank of the pages are: ')
    for rank in PR:
        print(rank)

ranker()
