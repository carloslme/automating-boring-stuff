#! python3
# lucky.py - Opens several Google search results

"""
After doing a Google search, you can see that the result page has a URL like https://www.google.com/search?q=SEARCH_TERM_HERE . 
The requests module can download this page and then you can use Beautiful Soup to find the search result links in the HTML. 
Finally, you’ll use the webbrowser module to open those links in browser tabs.
"""

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

print(res)

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.