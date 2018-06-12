import requests as req


def getSearchResults(search_query):
    google_api_key = "AIzaSyAFEtOQSFq-rVfu4QavaOtG7vAhm7hEb0M"
    custom_search_engine_id = "008822455400640800027:rqfvnddy_ou"

    url = 'https://www.googleapis.com/customsearch/v1?key='+google_api_key+\
          '&cx='+custom_search_engine_id+'&q='+search_query+''

    res = req.get(url)

    return res.json()["searchInformation"]["totalResults"]


print(getSearchResults("thishani"))
