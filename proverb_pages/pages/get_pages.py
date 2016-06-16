#! /usr/bin/python


import requests
import time
import sys

with open('urls.txt') as f:
    content = f.read()
    urls = content.split('\n')


counter = 0
headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
        'Accept': '*/*', 'User-Agent': 'I_just_want_some_provebs-kovykmax@gmail.com/1.0'}

for url in urls:
    sys.stdout.write('Downloading page n. {}  '.format(str(counter)))
    with open('page_{}.html'.format(str(counter)), 'w') as f:
        r = requests.get(url, headers=headers)
        f.write(r.text)

    sys.stdout.write('DONE, waiting....\n')
    time.sleep(10)

    counter += 1
