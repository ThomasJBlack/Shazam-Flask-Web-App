import requests


def requestFunc(inputPeram, endpoint):
    if endpoint == "search":
        querystring = {"term": inputPeram,
                       "locale": "en-US", "offset": "0", "limit": "10"}
    else:
        querystring = {"key": inputPeram, "locale": "en-US"}
    url = f"https://shazam.p.rapidapi.com/{endpoint}"

    headers = {
        'x-rapidapi-key': "42af4f16cfmsh688b43669c6f3c6p1615cbjsn2651aa62d88b",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response.json()
    