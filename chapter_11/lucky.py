#! python3
# lucky.py - Opens several Google search results

"""
After doing a Google search, you can see that the result page has a URL like https://www.google.com/search?q=SEARCH_TERM_HERE . 
The requests module can download this page and then you can use Beautiful Soup to find the search result links in the HTML. 
Finally, you’ll use the webbrowser module to open those links in browser tabs.
"""

"""import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.
soup = bs4. BeautifulSoup(res.text, 'html.parser')
#print('[INFO] ' + soup.prettify())
# Open a browser tab for each result.
linkElems = soup.select('.r a') # It looks like the r class is used only for search result links.

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))"""

import requests
from bs4 import BeautifulSoup as bs

urls = ['https://www.amazon.com/s?k=bacopa&page=1']

with requests.Session() as s:
    for url in urls:
        r = s.get(url, headers = {'User-Agent' : 'Mozilla/5.0'})
        soup = bs(r.content, 'lxml')
        listings = soup.find(id="suggestions-template")
        print(listings)
        print(len(listings))