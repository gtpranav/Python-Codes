# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:07:20 2017

@author: Pranav
"""

import urllib2
import pandas as pd
from bs4 import BeautifulSoup

link = "https://play.google.com/store/apps/details?id=com.ag.towerbuilder&hl=en"
page = urllib2.urlopen(link)

soup = BeautifulSoup(page)

list_reviews = soup.find_all('div', class_ = 'review-body with-review-wrapper')
list_ratings = soup.find_all('div', class_='tiny-star star-rating-non-editable-container')


ratings = []
reviews = []
for rating in list_ratings:
    rating = str(rating)
    init = rating.find("Rated")
    final = rating.find("five stars")+11
    ratings.append(rating[init:final])
    
#print ratings

for review in list_reviews:
    reviews.append(review.text)

a = []
df = pd.DataFrame()
df['Ratings'] = ratings
df['Reviews'] = reviews
    
print df
#print reviews

    