# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:53:06 2017

@author: Fitec
"""

import urllib
import bs4
import collections
import pandas as pd


req = urllib.request.Request('http://pokemondb.net/pokedex/national', headers = {'User-Agent' : 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
page = bs4.BeautifulSoup(html, "lxml")


liste_pokemon =[]
for pokemon in page.findAll('span', {'class' : 'infocard-tall'}) :
    pokemon = pokemon.find('a').get('href').replace("/pokedex/",'')
    liste_pokemon.append(pokemon)

###########################
pokemon= page.find('span', {'class' : 'infocard-tall'})
FindPok=pokemon.find('a').get('href').replace("/pokedex/",'')
###########################

def get_page(pokemon_name):
    url_pokemon = 'http://pokemondb.net/pokedex/'+ pokemon_name
    req = urllib.request.Request(url_pokemon, headers = {'User-Agent' : 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    return bs4.BeautifulSoup(html, "lxml")


def get_cara_pokemon(pokemon_name):
    page = get_page(pokemon_name)
    data = collections.defaultdict()


    for table in page.findAll('table', { 'class' : "vitals-table"})[0:4] :
        table_body = table.find('tbody')
        for rows in table_body.findChildren(['tr']) :
            if len(rows) > 1 : # attention aux tr qui ne contiennent rien
                column = rows.findChild('th').getText()
                cells = rows.findChild('td').getText()
                cells = cells.replace('\t','').replace('\n',' ')
                data[column] = cells
                data['name'] = pokemon_name
    return dict(data)

items = []
for e, pokemon in enumerate(liste_pokemon) :
    print(e, pokemon)
    item = get_cara_pokemon(pokemon)
    items.append(item)
    if e > 20:
        break
df = pd.DataFrame(items)
df.head()




import shutil
import requests


for e, pokemon in enumerate(liste_pokemon) :
    print(e,pokemon)
    url = "https://img.pokemondb.net/artwork/{}.jpg".format(pokemon)
    response = requests.get(url, stream=True)
    with open('{}.jpg'.format(pokemon), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    if e > 20:
        break