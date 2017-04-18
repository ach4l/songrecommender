import urllib2 as web
import re
#import os.mkdir
#Here we construct the database of songs to be searched on songmeanings
def songdirectory():
    songfile=open('songlist.txt','r')
    songlist=songfile.readlines()
    songdirectory={}
    for line in songlist:
        line=line[0:-1]
        song=line.split("\t") 
        try:
            songdirectory[song[2]] += '-'+song[1]
        except KeyError:
            songdirectory[song[2]] = song[1]
    #Here we search the songs in the directory (Band - Songs) in the songmeanings database to extract interpretations
  #  for artist in songdirectory:
        #artist2=artist.replace(', ','%20')
    artist2='bob%20dylan'
    webartistsongs=web.urlopen("http://songmeanings.com/query/?query={:s}&type=artists".format(artist2))
        #Just in case there are many results for band, then choose the first one (the most popular)
    for line in webartistsongs.readlines():
        artist="Bob Dylan"
        if '<tr class="item">' in line:
            if """title="{:s}">{:s}""".format(artist, artist) in line:
                url=line.split('"')[1]
                webartistsongs = web.urlopen(line.split('"')[1])
                print url             
                
            

    
    ##for artist in songdirectory:
    #    #artist=artist.replace(', ','%20')
    #    artist='Bob%20Dylan'
    #    websongs=web.urlopen("http://songmeanings.com/query/?query={:s}&type=artists".format(artist))
    
    return songdirectory, webartistsongs