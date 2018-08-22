#! python3
# imgur.py - Donwloads all preview images from Imgur.

from bs4 import BeautifulSoup
import requests
import os


def scrape_imgur():
    os.makedirs('imgur', exist_ok=True)
    search = input("Enter search criteria: \n")
    url = "https://imgur.com/search/score/all?q=" + search
    res = requests.get(url)                          # Download the page - response object.
    res.raise_for_status()                           # Is the URL valid?
    soup = BeautifulSoup(res.text, 'html.parser')

    for link in soup.find_all('img'):
        picture_url = link.get('src')                # Find an attribute 'src' in an <img> element.

        if picture_url.startswith('//i') is True:    # Check if the picture is related - starts with '//i'.
            picture_url = 'http:' + picture_url      # Get full address of the image.
            print(f'Downloading {picture_url}...')
            res = requests.get(picture_url)          # Download the image - response object.

            save = os.path.join('imgur', os.path.basename(picture_url))
            image_file = open(save, 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


scrape_imgur()

