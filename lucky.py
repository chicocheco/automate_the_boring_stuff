#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve from_top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
link_elems = soup.select('.r a')
# Find all <a> elements that are within an element that has the r ('.r') CSS class.

num_open = min(5, len(link_elems))
# min() returns the smallest of two or more arguments (or the smallest item in an iterable).
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
    # For ex. link_elems[0] is a link with index[0]
