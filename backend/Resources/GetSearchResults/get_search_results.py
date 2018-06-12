import requests as req


def getSearch(search_query):
    google_api_key = "AIzaSyAFEtOQSFq-rVfu4QavaOtG7vAhm7hEb0M"
    
    custom_search_engine_id = "008822455400640800027:rqfvnddy_ou"
    
    url = 'https://www.googleapis.com/customsearch/v1?key='+google_api_key+\
          '&cx='+custom_search_engine_id+'&q='+search_query+''
    
    res = req.get(url)
    
    return res.json()


def getSearchResults(search_query):
    return getSearch(search_query)["searchInformation"]["totalResults"]

def getImdbURL(search_query):    
    for item in getSearch(search_query)["items"]:
        try:
            if item["link"].index("imdb"):
                return item["link"]
        except Exception as ex:
            pass
    return "Not Found"

print(getSearchResults(("\"Bahubali 2\"")))
print(getImdbURL(("\"Bahubali 2\"")))
