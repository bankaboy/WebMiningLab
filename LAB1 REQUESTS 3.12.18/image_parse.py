import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
#values = {'s':'basics','submit':'search'}
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

respData = str(respData)
images = re.findall(r'<img(.*?)>',respData)

#images = re.findall(r'<img(.*?) src=(.*?)></',str(respData))

#print(images)

f = open("results.txt",'w')

for p in images:
    print(p)
    print('\n')
    f.write(str(p)+'\n')

f.close()

