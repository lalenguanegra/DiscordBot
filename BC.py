import requests
with open('webpage.txt', 'r') as myfile:
  data = myfile.read()
print(data)
r = requests.get(data, allow_redirects=True)
open('content.txt', 'wb').write(r.content)


import re 
infile = open('content.txt','r', encoding='latin-1')
read = infile.read()
result = re.search('mp3-128":"(.*)"},', read)
print(result.group(1))

import urllib.request
urllib.request.urlretrieve((result.group(1)), '1.mp3')

