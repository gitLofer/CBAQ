import json
import requests

def geo(city,lang):
    r = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+city+"&key=62a752a9a17d47db88fcf4b4576783d6")
    j = r.json()
    if j['total_results'] == 0:
        if lang == "EN":
            return "We don't have data for that city yet"
        elif lang == "RS":
            return "Trenutno nemamo podatke za taj grad"
    else:
        return "Lat: " + str(j['results'][0]['geometry']['lat']) + '\nLng: ' + str(j['results'][0]['geometry']['lng'])

def aqi (city, lang):
    r = requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j = r.json()
    if j['status'] != "ok" or j['data']['aqi'] == '-':
        if lang == "EN":
            return "We don't have data for that city yet"
        elif lang == "RS":
            return "Trenutno nemamo podatke za taj grad"
    else:
        if lang == 'EN':
            k = j['data']['aqi']
            int(k)
            if k <= 50:
                return ('Air quality index is: ', str(k), "\nIt's good air quality (green zone)")
            elif k <= 100:
                return ('Air quality index is: ', str(k), "\nIt's moderate air quality (yellow zone)")
            elif k <= 150:
                return ('Air quality index is: ', str(k), "\nIt's unhealthy air quality for sensiteve groups (orange zone)")
            elif k <= 200:
                return ('Air quality index is: ', str(k), "\nIt's unhealthy air quality (red zone)")
            elif k <= 300:
                return ('Air quality index is: ', str(k), "\nIt's very unhealthy air quality (blue zone)")
            else:
                return ('Air quality index is: ', str(k), "\nIt's hazardous air quality (violet zone)")
        elif lang == 'RS':
            k = j['data']['aqi']
            int(k)
            if k <= 50:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo je dobar kvalitet vazduha (zelena zona)")
            elif k <= 100:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo je umeren kvalitet vazduha (zuta zona)")
            elif k <= 150:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo nije zdrav kvalitet vazduha za osetljive grupe (narandzasta zona)")
            elif k <= 200:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo nije zdrav kvalitet vazduha (crvena zona)")
            elif k <= 300:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo bas nije zdrav kvalitet vazduha (plava zona)")
            else:
                return ('Indeks kvalitet vazduha iznosi: ', str(k), "\nTo je opasan kvalitet vazduha, koliko je los (ljubicasta zona)")


def uviTrenutno(city, language):
    r = requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j = r.json()
    r2 = requests.get("https://api.waqi.info/feed/Zagreb/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j2 = r2.json()

    i = 0
    while j['data']['forecast']['daily']['uvi'][i]['day'] != j2['data']['forecast']['daily']['uvi'][0]['day']:
        i += 1

    if language == 'RS':
        if j['status'] == 'error':
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok':
            k = j['data']['forecast']['daily']['uvi'][i]['max']
            int(k)
            if k <= 3:
                return ('Maksimalni UV indeks je: ',str(k),'\nNiska opasnost od UV zracenja - Zelena zona')
            elif k <= 6:
                return('Maksimalni UV indeks je: ',str(k),'\nSrednji rizik od UV zracenja - Zuta zona','\nPreporuka: Potrudite se da ne izlazite na Sunce oko podneva')
            elif k <= 8:
                return('Maksimalni UV indeks je: ',str(k),'\nVisok rizik od UV zracenja - Narandzasta zona','\nPreporuka: Nosite naocare za suncanje i kremu sa zastitnim faktorom 30+')
            elif k <= 10:
                return('Maksimalni UV indeks je: ',str(k),'\nVeoma visok rizik od UV zracenja - Crvena zona','\nPreporuka: Nemojte ostajati dugo na Suncu i nanosite kremu sa zastitnim faktorom 30+')
            elif k >= 11:
                return('Maksimalni UV indeks je: ',str(k),'\nEkstremni rizik od UV zracenja - Ljubicasta zona','\nPreporuka: Izbegavajte Sunce od 10h do 17h i zastitite celu kozu sa adekvatnim oblacenjem')
    elif language == 'EN':
        if j['status'] == 'error':
            return "We don't have information for that city"
        elif j['status'] == 'ok':
            k=j['data']['forecast']['daily']['uvi'][i]['max']
            int(k)
            if k <= 3:
                return('The maximum UV index is: ' , str(k),'\nLow risk of UV radiation - Green zone')
            elif k <= 6:
                return('The maximum UV index is: ' , str(k),'\nMedium risk of UV radiation - Yellow zone','\nAdvice: Try not to go out in the sun around noon')
            elif k <= 8:
                return('The maximum UV index is: ' , str(k),'\nHigh risk of UV radiation - Orange zone','\nAdvice: Wear sunglasses and tanning cream with a protection factor of 30+')
            elif k <= 10:
                return('The maximum UV index is: ' , str(k),'\nVery high risk of UV radiation - Red zone',"\nAdvice: Wear tanning cream with a protection factor of 30+ and don't stay long on the sun")
            elif k >= 11:
                return('The maximum UV index is: ' , str(k),'\nExtreme risk of UV radiation - Violet zone',"\nAdvice: Avoid the sun from 10am to 5pm and protect your skin with clothes")
            return

def uviZaNarednaTriDana(city, language):
    r = requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j = r.json()
    r2 = requests.get("https://api.waqi.info/feed/Zagreb/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j2 = r2.json()

    i=1
    while j['data']['forecast']['daily']['uvi'][i]['day'] != j2['data']['forecast']['daily']['uvi'][1]['day'] :
        i += 1

    if language == 'RS':
        if j['status'] == 'error' :
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok' :
            a = j['data']['forecast']['daily']['uvi'][i]['max']
            b = j['data']['forecast']['daily']['uvi'][i+1]['max']
            c = j['data']['forecast']['daily']['uvi'][i+2]['max']
            x = j['data']['forecast']['daily']['uvi'][i]['day']
            y = j['data']['forecast']['daily']['uvi'][i+1]['day']
            z = j['data']['forecast']['daily']['uvi'][i+2]['day']
            return ('\nMax UVI za ', str(x), ' je ', str(a), '\nMax UVI za ', str(y), ' je ', str(b), '\nMax UVI za ', str(z), ' je ', str(c) )
    elif language == 'EN':
        if j['status'] == 'error':
            return "We don't have information for that city"
        elif j['status'] == 'ok':
            a = j['data']['forecast']['daily']['uvi'][i]['max']
            b = j['data']['forecast']['daily']['uvi'][i+1]['max']
            c = j['data']['forecast']['daily']['uvi'][i+2]['max']
            x = j['data']['forecast']['daily']['uvi'][i]['day']
            y = j['data']['forecast']['daily']['uvi'][i+1]['day']
            z = j['data']['forecast']['daily']['uvi'][i+2]['day']

            return ('Max UVI for ', str(x), ' is ', str(a), '\nMax UVI for ', str(y), ' is ', str(b), '\nMax UVI for ', str(z), ' is ', str(c))
