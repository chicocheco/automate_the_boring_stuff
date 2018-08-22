#! python3
# scraping_xkcd.py - Downloads every single XKCD comic.

import bs4
import os
import requests

url = 'http://xkcd.com'                     # starting url
os.makedirs('xkcd', exist_ok=True)          # store comics in .\xkcd (if the folder already exists, it's fine)
while not url.endswith('#'):                # https://xkcd.com/1/# is the very last page, clicking on 'PREV' button
    print(f'Downloading page {url}...')
    res = requests.get(url)                 # response object - download the page
    res.raise_for_status()                  # doesn't do anything if the download succeded

    soup = bs4.BeautifulSoup(res.text, "html.parser")      # beautifulsoup object from the text of the downloaded page
    comic_elem = soup.select('#comic img')  # select <img> element inside <div> element with id='comic'

    if not comic_elem:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + comic_elem[0].get('src')

            # Download the image.
            print(f'Downloading image {comic_url}...')      # example: http: + //imgs.xkcd.com/comics/comic_image.jpg
            res = requests.get(comic_url)                   # response object - download the image
            res.raise_for_status()                          # if the download failed, continue to the 'exception'
        except requests.exceptions.MissingSchema:           # (http or https is missing)

            # FAILED. Get the Prev button's url to continue iterating and try to find a comic again.
            prev_link = soup.select('a[rel="prev"]')[0]      # select <a> element with rel="prev" attribute
            url = 'http://xkcd.com' + prev_link.get('href')  # URL for the next iteration of the WHILE NOT loop
            continue                                         # jump back to the start of the WHILE NOT loop

        # Save the image to .\xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')  # like .\xkcd\comic_image.png
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        # !! this is the end of ELSE clause !!

    # SUCCESS. Get the Prev button's url to continue iterating and find another comic.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')          # URL for the next iteration of WHILE NOT loop

print('Done.')


"""
Errors can be handled with TRY and EXCEPT statements. 
The code that could potentially have an error is put in a try clause. 
The program execution moves to the start of a following except clause if an error happens.



Selector passed to the select() method - Will match...

soup.select('div') - All elements named <div>.
soup.select('#author') - The element with an id attribute of author.
soup.select('.notice') - All elements that use a CSS class attribute named notice.
soup.select('div span') - All elements named <span> that are within an element named <div>.
soup.select('div > span') - All elements named <span> that are directly within an element named <div>, 
                            with no other element in between.
soup.select('input[name]') - All elements named <input> that have a name attribute with any value.
soup.select('input[type="button"]') - All elements named <input> that have an attribute named type with value button.
"""
