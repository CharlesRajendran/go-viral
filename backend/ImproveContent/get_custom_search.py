import requests as req


def getSearch(search_query):
    
    # #charles key
    # google_api_key = "AIzaSyAFEtOQSFq-rVfu4QavaOtG7vAhm7hEb0M"
    # custom_search_engine_id = "008822455400640800027:rqfvnddy_ou"
    

    
    #thishani key
    # google_api_key = "AIzaSyDLZOGgYNPz7Acxc6s_f84CQ3TGt93IUuQ"
    # custom_search_engine_id = "008498746748925297721:j4aqmfalkdg" 
    
    #ctt key
    google_api_key = "AIzaSyDLIImEv5J-aMargxkQyUjue0iOtzJf-z4"
    custom_search_engine_id = "014472105597825897847:1hzwsjxkeym" 


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


if __name__ == "__main__":
    print(getSearch("Wonder Woman"))
    print(getImdbURL("Wonder Woman"))
    print(getSearchResults("Wonder Woman"))
