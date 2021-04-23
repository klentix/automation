# First Spider

import pandas as pd
import numpy as np

import requests
from requests import get
from bs4 import BeautifulSoup

from time import sleep
from random import randint

# Creating the lists of fields we want to record
# titles = []
movieStars = []
movieDirector = []

# Capturing English translated movie titles
headers = {'Accept-Language': 'en-US, en;q=0.5'}

pages = np.arange(1, 1001, 50)

# Storing each of the urls of 50 movies
for page in pages:
    # Getting the contents from the each url
    page = requests.get('https://www.imdb.com/search/title/?groups=top_1000&start=' + str(page) + '&ref_=adv_nxt',
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Navigating to the part of the html for info we need
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')

    # Controlling the loop’s rate by pausing the execution of the loop for a specified amount of time
    # Add random delays between the queries sent to Google to avoid getting blocked in python
    # Waiting time between requests for a number between 2-10 seconds
    sleep(randint(2, 10))

    for movie in movie_div:
        # Scraping the movie's title
        # name = movie.h3.a.text
        # titles.append(name)

        # Scraping the actor's names & director's names
        movieCast = movie.find("p", class_="")
        try:
            casts = movieCast.text.replace("\n", "").split('|')
            casts = [x.strip() for x in casts]
            casts = [casts[i].replace(j, "") for i, j in enumerate(["Director:", "Stars:"])]
            movieDirector.append(casts[0])
            movieStars.append([x.strip() for x in casts[1].split(",")])
        except:
            casts = movieCast.text.replace("\n", "").strip()
            movieDirector.append(np.nan)
            movieStars.append([x.strip() for x in casts.split(",")])

        movies = pd.DataFrame({
            'director': movieDirector,
            'cast': movieStars})

        movies.head()
        # movies.dtypes
        movies.to_csv('movie.csv', index=False)
