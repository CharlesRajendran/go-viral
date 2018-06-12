from nltk.tokenize import word_tokenize as wt
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import math
import os
import getmovielist

movie_name = ""
total_reviews = 0
total_pages = 0
current_page = 0
popular_count = 1
non_popular_count = 1

def get_details(url_arg):
    url = urlopen(url_arg)
    html = url.read()
    url.close()

    soup = bs(html,"html.parser")
    
    movie_name = " ".join(wt(soup.title.get_text())[:wt(soup.title.get_text()).index('Reviews')])
    total_reviews = int(wt(soup.find(align="right").get_text())[0])
    total_pages = math.ceil(total_reviews/10)

    return (movie_name,total_reviews,total_pages)
    
def createFolders(name):
    try:
        os.mkdir('Movies')
        os.mkdir('Movies/popular')
        os.mkdir('Movies/non-popular')
    except Exception as e:
        return 0

def generateDOcument(name,content):
    file_name = 'Movies/'+name+'.txt'
    file_handler = open(file_name,"w")
    file_handler.write(content)
    file_handler.close()
    
    
def scrape_page(url_arg):
    url = urlopen(url_arg)
    html = url.read()
    url.close()

    soup = bs(html,"html.parser")

    global popular_count
    global non_popular_count
    
    # scrape reviews
    reviews = re.findall(r'<hr (.*?)</p>',str(html))

    
    for r in reviews[1:-1]:
        soup_review = bs(r,"html.parser")
        
        review_text = soup_review.find("p")
        review_final_text = review_text.get_text().replace("\\n","")
        
        if str(review_final_text) != "*** This review may contain spoilers ***":
            try:
                review_likes = int(wt(soup_review.find("small").get_text())[0])
                review_interests = int(wt(soup_review.find("small").get_text())[3])
                like_ratio = review_likes/review_interests
                interest_ratio = review_interests/int(total_reviews)
                
            except Exception as e:
                print("Exception",e)
                continue
            
            if interest_ratio > 0.50:
                if like_ratio > 0.80 and review_likes > 10:
                    review_name = 'popular/'+str(popular_count)
                    popular_count = popular_count + 1
                    review_content = "{0}\n=============\nlike ratio : {1}\ninterest ratio: {2}\nmoviename: {3}\nnumber of likes: {4}\nnumber of interests : {5}".format(review_final_text,like_ratio,interest_ratio,movie_name,review_likes,review_interests)
                    generateDOcument(review_name,review_content)
                    
                elif like_ratio < 0.35:
                    review_name = 'non-popular/'+str(non_popular_count)
                    non_popular_count = non_popular_count+1
                    review_content = "{0}\nlike ratio : {1}\ninterest ratio: {2}".format(review_final_text,like_ratio,interest_ratio)
                    generateDOcument(review_name,review_content)
                    
            else:
                if like_ratio > 0.9 and review_likes > 20:
                    review_name = 'popular/'+str(popular_count)
                    popular_count = popular_count + 1
                    review_content = "{0}\nlike ratio : {1}\ninterest ratio: {2}".format(review_final_text,like_ratio,interest_ratio)
                    generateDOcument(review_name,review_content)
                        
                elif like_ratio < 0.45:
                    review_name = 'non-popular/'+str(non_popular_count)
                    non_popular_count = non_popular_count +1
                    review_content = "{0}\nlike ratio : {1}\ninterest ratio: {2}".format(review_final_text,like_ratio,interest_ratio)
                    generateDOcument(review_name,review_content)



def crawl(movie_id):

    review_url = "http://www.imdb.com/title/{0}/reviews".format(movie_id)
    global movie_name
    global total_reviews
    global total_pages
    global current_page
    movie_name, total_reviews, total_pages = get_details(review_url)
    createFolders(movie_name)

    for page_number in range(total_pages):
        arg_url = review_url+"?start={0}".format(page_number*10)
        current_page = page_number
        scrape_page(arg_url)


def init():
    movie_list = getmovielist.return_ids()
    for movie in movie_list[10:30]:
        crawl(movie)
        
init()
