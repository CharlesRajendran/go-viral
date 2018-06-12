from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize as wt

from urllib.request import urlopen
import re
import math
import os

from get_ids import readFile as rf

movie_name = ""
total_reviews = 0
total_pages = 0
current_page = 0
popular_count = 1
non_popular_count = 1

def createFolders():
    try:
        os.mkdir('Movies')
        os.mkdir('Movies/popular')
        os.mkdir('Movies/non-popular')
    except Exception as e:
        pass

def generateDOcument(name,content):
    file_name = 'Movies/'+name+'.txt'
    file_handler = open(file_name,"w")
    file_handler.write(content)
    file_handler.close()

def get_details(movie_url):
    print(movie_url)
    url = urlopen(movie_url)
    html = url.read()
    url.close()
    
    soup = bs(html,"html.parser")
        
    movie = " ".join(wt(soup.title.get_text())[:wt(soup.title.get_text()).index("Reviews")])
    total_reviews = int(wt(soup.find(align="right").get_text())[0])
    total_pages = int(math.ceil(total_reviews/10))

    return (movie,total_reviews,total_pages)

def scrape_page(url_arg):
    try:
        url = urlopen(url_arg)
        html = url.read()
        url.close()
    except Exception as e:
        pass


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
                print(e)
                continue
            
            if interest_ratio > 0.50:
                if like_ratio > 0.8 and review_likes > 10:
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
                if like_ratio > 0.90 and review_likes > 20:
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
    (movie_name, total_reviews, total_pages) = get_details(review_url)
    
    print(movie_name, total_reviews, total_pages)
    createFolders()
    
    if total_reviews > 5:    
        for page_number in range(total_pages):
            arg_url = review_url+"?start={0}".format(str(page_number*10))
            current_page = page_number
            scrape_page(arg_url)

        print("good",movie_id,"\n")
    else:
        print("not good",movie_id,"\n")
        
def init():
    movielist = rf()
    for movie in movielist[:7000]:
        try:
            crawl(movie)
        except Exception as e:
            continue
        
init()
