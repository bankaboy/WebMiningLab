#from nigger import slave
from pprint import pprint

weblog = [
    ['1','1.2.3.4','A','','IE5;Win2k'],
    ['9','1.2.3.4','B','A','IE5;Win2k'],
    ['10','2.3.4.5','C','','IE5;Win98k'],
    ['12','2.3.4.5','B','C','IE5;Win98k'],
    ['15','2.3.4.5','E','C','IE5;Win98k'],
    ['19','1.2.3.4','C','A','IE5;Win2k'],
    ['22','2.3.4.5','D','B','IE5;Win98k'],
    ['22','1.2.3.4','A','','IE5;Win98k'],
    ['25','1.2.3.4','E','C','IE5;Win2k'],
    ['25','1.2.3.4','C','A','IE5;Win98k'],
    ['33','1.2.3.4','B','C','IE5;Win98k'],
    ['58','1.2.3.4','D','B','IE5;Win98k'],
    ['70','1.2.3.4','E','D','IE5;Win98k'],
    ['75','1.2.3.4','A','','IE5;Win2k'],
    ['76','1.2.3.4','C','A','IE5;Win2k'],
    ['77','1.2.3.4','F','C','IE5;Win98k'],
    ['85','1.2.3.4','F','C','IE5;Win2k'],
    ['90','1.2.3.4','B','A','IE5;Win2k'],
    ['96','1.2.3.4','D','B','IE5;Win2k']
]

session1, session2, session3 = [], [], []
refering1, refering2, refering3 = [], [], []
url1, url2, url3 = [], [], []
for record in weblog:
    if record[1] == '1.2.3.4':
        if record[4] == 'IE5;Win2k':
            session1.append(record)
        else:
            session2.append(record)
    else:
        session3.append(record)

pprint(session1)
print('\n')
pprint(session2)
print('\n')
pprint(session3)

for record in session1:
    url1.append(record[2])
    refering1.append(record[3])

for record in session2:
    url2.append(record[2])
    refering2.append(record[3])    

for record in session3:
    url3.append(record[2])
    refering3.append(record[3])
    
print("\nSESSION 1 :\n")
pprint(url1)
pprint(refering1)

print("\nSESSION 2 :\n")
pprint(url2)
pprint(refering2)

print("\nSESSION 3 :\n")
pprint(url3)
pprint(refering3)

    
