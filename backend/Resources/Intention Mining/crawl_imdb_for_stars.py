import get_custom_search as gcs

from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize as wt

from urllib.request import urlopen

import movie_tweets as mt 

#print(gcs.getSearchResults(("\"Theri\"")))
print(gcs.getImdbURL(("\"Theri\"")))

def returnMovieCelebratiesWithPopularity(movie_name):

    imdburl = gcs.getImdbURL(movie_name)
    celeberaties = []
    final_keywords = []

    if imdburl != "Not Found":
        url_o = urlopen(imdburl)
        html_src = url_o.read()
        url_o.close()

        soup = bs(html_src,"html.parser")

        movie_popularity = int(gcs.getSearchResults(movie_name))

        for div in soup.findAll("div",{"class":"credit_summary_item"}):
            links = bs(str(div),"lxml").a
            name = links.span.getText()
            celeberaties.append((name,int(gcs.getSearchResults(name))/movie_popularity))
    
        for (actor,popular) in celeberaties:
            if popular > 1:
                final_keywords.append(actor)

    final_keywords_with_movie = [movie_name]+list(set(final_keywords))

    return final_keywords_with_movie

if __name__ == "__main__":
    print(returnMovieCelebratiesWithPopularity("Wonder Woman"))
    mt.getTweets(returnMovieCelebratiesWithPopularity("Wonder Woman"))
