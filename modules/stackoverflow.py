from datetime import datetime

import requests

API_URL = "https://api.stackexchange.com/2.2"

def stackoverflow(userid):
    req = requests.get("%s/users/%s" % (API_URL, userid), 
                       params={"site": "stackoverflow.com"})
    d = req.json()["items"][0]

    dates = [i for i in d if i.endswith("_date")]
    for date in dates:
        d[date] = datetime.fromtimestamp(d[date])

    return d

MAIN = stackoverflow
