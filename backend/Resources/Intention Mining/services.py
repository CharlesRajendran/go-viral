from bottle import run, get, post,request, delete
import direct_message_api as dma
import intention_mining as im



print('Server Started at post 8080....')

movie_name = ""
review_url = ""

@get('/tweets')
def get_tweets():
    movie_tweets = "data/{0}/{0}.csv".format(movie_name)
    return {"tweets":dma.takeIntentTweets(movie_tweets),"review_url":review_url,"movie_name":movie_name}

@post('/post_review')
def post_review():
    movie = request.json.get('movie')
    content = request.json.get('content')
    global movie_name
    global review_url
    movie_name = movie
    
    re_url = im.post_review_backend(movie,content)
    review_url = re_url

    return {"movie_name":movie,"reviewUrl":re_url}



@post('/tweeter_message')
def tweeter_message():
    screen_name = request.json.get('screen_name')
    message = request.json.get('message')
    
    response = dma.send(screen_name,message)

    return {"status":response}

run(reloader=True,debug=True)
