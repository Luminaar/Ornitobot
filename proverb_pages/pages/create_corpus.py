#! /usr/bin/python

from bs4 import BeautifulSoup as BS


with open('corpus.txt', 'w') as corpus:

    for i in range(348):
        print 'Currently on page {}'.format(str(i))

        with open('page_{}.html'.format(str(i))) as page:

            text = page.read()

            soup = BS(text)

            for p in soup.find_all('p')[:-2]:

                proverb = p.text
                proverb = proverb.replace('\r', '')
                corpus.write(proverb)
                corpus.write('\n')
