import json
import requests

def uviTrenutno(city, language):
    r= requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j= r.json()

    if language == 'RS':
        if j['status'] == 'error' :
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok' :
            k=j['data']['forecast']['daily']['uvi'][0]['max']
            int(k)
            if k <= 3:
                return ('Maksimalni UV indeks je: ',str(k),'Niska opasnost od UV zracenja - Zelena zona')
            elif k<=6:
                return('Maksimalni UV indeks je: ',str(k),'Srednji rizik od UV zracenja - Zuta zona','Preporuka: Potrudite se da ne izlazite na Sunce oko podneva')
            elif k<=8:
                return('Maksimalni UV indeks je: ',str(k),'Visok rizik od UV zracenja - Narandzasta zona','Preporuka: Nosite naocare za suncanje i kremu sa zastitnim faktorom 30+')
            elif k<=10:
                return('Maksimalni UV indeks je: ',str(k),'Veoma visok rizik od UV zracenja - Crvena zona','Preporuka: Nemojte ostajati dugo na Suncu i nanosite kremu sa zastitnim faktorom 30+')
            elif k>=11:
                return('Maksimalni UV indeks je: ',str(k),'Ekstremni rizik od UV zracenja - Ljubicasta zona','Preporuka: Izbegavajte Sunce od 10h do 17h i zastitite celu kozu sa adekvatnim oblacenjem')
    elif language == 'ENG':
        if j['status'] == 'error' :
            return "We don't have information for that city"
        elif j['status'] == 'ok' :
            k=j['data']['forecast']['daily']['uvi'][0]['max']
            print('The maximum UV index is: ' + k)
            int(k)
            if k <= 3:
                return('The maximum UV index is: ' , str(k),'Low risk of UV radiation - Green zone')
            elif k<=6:
                return('The maximum UV index is: ' , str(k),'Medium risk of UV radiation - Yellow zone','Advice: Try not to go out in the sun around noon')
            elif k<=8:
                return('The maximum UV index is: ' , str(k),'High risk of UV radiation - Orange zone','Advice: Wear sunglasses and tanning cream with a protection factor of 30+')
            elif k<=10:
                return('The maximum UV index is: ' , str(k),'Very high risk of UV radiation - Red zone',"Advice: Wear tanning cream with a protection factor of 30+ and don't stay long on the sun")
            elif k>=11:
                return('The maximum UV index is: ' , str(k),'Extreme risk of UV radiation - Violet zone',"Advice: Avoid the sun from 10am to 5pm and protect your skin with clothes")
            return

def uviZaNarednaTriDana(city, language):
    r = requests.get("https://api.waqi.info/feed/" + city + "/?token=e95e9dd0a620f4d84415424d036fc493e4059e45")
    j = r.json()

    if language == 'RS':
        if j['status'] == 'error' :
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok' :
            a=j['data']['forecast']['daily']['uvi'][1]['max']
            b=j['data']['forecast']['daily']['uvi'][2]['max']
            c=j['data']['forecast']['daily']['uvi'][3]['max']

            x = j['data']['forecast']['daily']['uvi'][1]['day']
            y = j['data']['forecast']['daily']['uvi'][2]['day']
            z = j['data']['forecast']['daily']['uvi'][3]['day']

            return('Max uvi za ', str(x), ' je ', str(a), 'Max uvi za ', str(y), ' je ', str(b), 'Max uvi za ', str(z), ' je ', str(c) )
    elif language == 'ENG':
        if j['status'] == 'error':
            return "We don't have information for that city"
        elif j['status'] == 'ok':
            a = j['data']['forecast']['daily']['uvi'][1]['max']
            b = j['data']['forecast']['daily']['uvi'][2]['max']
            c = j['data']['forecast']['daily']['uvi'][3]['max']
            x = j['data']['forecast']['daily']['uvi'][1]['day']
            y = j['data']['forecast']['daily']['uvi'][2]['day']
            z = j['data']['forecast']['daily']['uvi'][3]['day']

            return ('Max uvi for ', str(x), ' is ', str(a), 'Max uvi for ', str(y), ' is ', str(b), 'Max uvi for ', str(z), ' is ',str(c))
