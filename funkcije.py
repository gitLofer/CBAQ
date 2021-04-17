import json
import requests
import discord
from datetime import datetime
from datetime import date
import time

def vremeTrenutno():
    today = date.today()
    d = today.strftime("%d/%m/%Y")
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return (d, current_time)

def geo(city,lang):
    r = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+city+"&key=62a752a9a17d47db88fcf4b4576783d6")
    j = r.json()
    if j['total_results'] == 0:
        if lang == "EN":
            return "We don't have data for that city"
        elif lang == "RS":
            return "Nemamo podatke za taj grad"
    else:
        if lang == 'EN':
            la = str(j['results'][0]['geometry']['lat'])
            ln = str(j['results'][0]['geometry']['lng'])
            vreme = vremeTrenutno()
            embed = discord.Embed(title="Geolocation", url="https://www.google.com/maps/@"+la+","+ln+",14z", color=0x6d51f5)
            embed.add_field(name="lat", value= la , inline=True)
            embed.add_field(name="lgn", value= ln , inline=True)
            embed.set_footer(text=vreme[0] + ", " + vreme[1])
            return embed
        elif lang == 'RS':
            la = str(j['results'][0]['geometry']['lat'])
            ln = str(j['results'][0]['geometry']['lng'])
            vreme = vremeTrenutno()
            embed = discord.Embed(title="Geolokacija", url="https://www.google.com/maps/@" + la + "," + ln + ",14z",color=0x6d51f5)
            embed.add_field(name="lat", value=la, inline=True)
            embed.add_field(name="lgn", value=ln, inline=True)
            embed.set_footer(text= vreme[0] + ", " + vreme[1])
            return embed
            #return "Lat: " + str(j['results'][0]['geometry']['lat']) + '\nLng: ' + str(j['results'][0]['geometry']['lng'])

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

    if language == 'RS':
        if j['status'] == 'error':
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok':
            Current_Date = datetime.date(datetime.now())
            i = 0
            while str(j['data']['forecast']['daily']['uvi'][i]['day']) != str(Current_Date):
                i += 1

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
            Current_Date = datetime.date(datetime.now())
            i = 0
            while str(j['data']['forecast']['daily']['uvi'][i]['day']) != str(Current_Date):
                i += 1

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

    if language == 'RS':
        if j['status'] == 'error':
            return 'Nemamo informacije za zadati grad'
        elif j['status'] == 'ok':
            Current_Date = datetime.date(datetime.now())
            i = 0
            while str(j['data']['forecast']['daily']['uvi'][i]['day']) != str(Current_Date):
                i += 1

            a = j['data']['forecast']['daily']['uvi'][i + 1]['max']
            b = j['data']['forecast']['daily']['uvi'][i + 2]['max']
            c = j['data']['forecast']['daily']['uvi'][i + 3]['max']
            x = j['data']['forecast']['daily']['uvi'][i + 1]['day']
            y = j['data']['forecast']['daily']['uvi'][i + 2]['day']
            z = j['data']['forecast']['daily']['uvi'][i + 3]['day']

            embed = discord.Embed(title = "Maksimalan UVI za naredna tri dana: ", color=0x0cca3b)
            embed.add_field(name=str(x), value=str(a), inline=True)
            embed.add_field(name=str(y), value=str(b), inline=True)
            embed.add_field(name=str(z), value=str(c), inline=True)
            return embed

            #return ('\nMax UVI za ', str(x), ' je ', str(a), '\nMax UVI za ', str(y), ' je ', str(b), '\nMax UVI za ', str(z), ' je ', str(c) )
    elif language == 'EN':
        if j['status'] == 'error':
            return "We don't have information for that city"
        elif j['status'] == 'ok':
            Current_Date = datetime.date(datetime.now())
            i = 0
            while str(j['data']['forecast']['daily']['uvi'][i]['day']) != str(Current_Date):
                i += 1

            a = j['data']['forecast']['daily']['uvi'][i+1]['max']
            b = j['data']['forecast']['daily']['uvi'][i+2]['max']
            c = j['data']['forecast']['daily']['uvi'][i+3]['max']
            x = j['data']['forecast']['daily']['uvi'][i+1]['day']
            y = j['data']['forecast']['daily']['uvi'][i+2]['day']
            z = j['data']['forecast']['daily']['uvi'][i+3]['day']

            embed = discord.Embed(title="Max UVI for next three days is: ", color=0x0cca3b)
            embed.add_field(name=str(x), value=str(a), inline=True)
            embed.add_field(name=str(y), value=str(b), inline=True)
            embed.add_field(name=str(z), value=str(c), inline=True)
            return embed

            #return ('Max UVI for ', str(x), ' is ', str(a), '\nMax UVI for ', str(y), ' is ', str(b), '\nMax UVI for ', str(z), ' is ', str(c))

def weather(city,language):
    err = ""

    if language == "RS":
        r = requests.get("https://api.weatherapi.com/v1/current.json?key=a85e144e4fa1496bba2100733211504&q=" + city + "&aqi=no&lang=sr")
        j = r.json()
        #title = "Vreme u gradu"
        try:
            return ("Vreme je ", j['current']['condition']['text'].lower(), ", tj. temperatura je ",str(j['current']['temp_c'])+" °C")
        except:
            err = "Trenutno nemamo podatke za taj grad"
        if err != "":
            return err
    elif language == "EN":
        r = requests.get("https://api.weatherapi.com/v1/current.json?key=a85e144e4fa1496bba2100733211504&q=" + city + "&aqi=no")
        j = r.json()
        #title = "Weather in"
        try:
            return ("Weather is ",j['current']['condition']['text'].lower(), "\nThe temperature is " + str(j['current']['temp_c']) + " °C")
        except:
            err = "We don't have data for that city yet."
        if err != "":
            return err

def weatherforecast(city,language):
    token = '881b48ca72047425e45c875edd0b8398'
    city = city.title()
    if language == "EN":
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + token)
        j = r.json()

        if j['cod'] != '200':
            return "We don't have data for that city yet."

        # j['list'][0]['dt_txt'] -> [11:13] -> int
        curr_time = int((j['list'][0]['dt_txt'])[11:13])
        print(curr_time)
        if curr_time == 12:
            start_pos = 0
        else:
            start_pos = abs((curr_time % 12) - 12) / 3

        target = []
        dates = []
        for i in range(1,5):
            curr = int(start_pos + i * 8)
            target.append(j['list'][curr]['weather'][0]['description'].capitalize() +
                           "\nAverage temperature: " + str( round ( j['list'][curr]['main']['temp'] - 273.15, 2)) + "°C")
            dates.append((j['list'][curr]['dt_txt'])[:16])
        title = "Weather forecast for " + city
        curr_txt = 'Current weather'

    elif language == "RS":
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + token + '&lang=sr')
        j = r.json()

        if j['cod'] != '200':
            return "Trenutno nemamo podatke za taj grad."

        curr_time = int((j['list'][0]['dt_txt'])[11:13])
        start_pos = abs((curr_time % 12) - 12) / 3

        target = []
        dates = []
        for i in range(1,5):
            curr = int(start_pos + i * 8)
            target.append(j['list'][curr]['weather'][0]['description'].capitalize() +
                          "\nProsecna temperatura: " + str(round(j['list'][curr]['main']['temp'] - 273.15, 2)) + "°C")
            dates.append((j['list'][curr]['dt_txt'])[:16])
        title = "Weather forecast for " + city
        curr_txt = 'Trenutno vreme'

    print(target)
    print(dates)
    embed = discord.Embed(title=title, color=0xff9500)
    vreme = vremeTrenutno()
    embed.add_field(name=curr_txt, value=target[0], inline=False)
    embed.add_field(name=dates[1], value=target[1], inline=True)
    embed.add_field(name=dates[2], value=target[2], inline=True)
    embed.add_field(name=dates[3], value=target[3], inline=True)
    embed.set_footer(text=vreme[0] + ", " + vreme[1])
    return embed
