import json
import requests

def geo(city,lang):
    j = {}
    r = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+city+"&key=62a752a9a17d47db88fcf4b4576783d6")
    j  = r.json()
    if j['total_results'] == 0 :
        if lang == "EN":
            return "We don't have data for that city yet"
        elif lang == "SR":
            return "Trenutno nemamo podatke za taj grad"
    else:
        return j['results'][0]['geometry']['lat'],j['results'][0]['geometry']['lng']

def aqi (city,lang):
    r = requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j = r.json()
    if j['status'] != "ok":
        if lang == "EN":
            return "We don't have data for that city yet"
        elif lang == "SR":
            return "Trenutno nemamo podatke za taj grad"
    else:
        return j['data']['aqi']

