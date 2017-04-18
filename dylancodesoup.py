# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 02:36:17 2017

@author: Raven
"""
from bs4 import BeautifulSoup
import urllib
import re
import requests
import os
from getcommentssoup import getcommentssoup



"""
This part takes the artist root page and extracts all the songnames and their links

IMPROVE - make the artist search automatic given the name of the artist
"""

dylanpage=urllib.request.urlopen('http://songmeanings.com/query/?query=bob%20dylan&type=songtitles')
dylanpagesoup=BeautifulSoup(dylanpage, "lxml")
#hreftest=re.compile('*')
Songs=dylanpagesoup.find_all("a", class_="", style_="", href=re.compile('songmeanings.com+'))


f=open('songnames','w')
for song in Songs:
    songname=song.get_text()
    url=song['href']
    #url=songtext.split('"')[5]
    #Seperated by semi colon
    f.writelines(url+';'+songname+'\n')
f.close()
fo=open('songnames','r')
ln=fo.readlines()
for il  in range(2,3):
    songpageadress=ln[il].split(";")[0]
    songname=ln[il].split(";")[-1]
    songname = songname.rstrip()
    #make directory here
    songpage=urllib.request.urlopen('http:'+songpageadress)
    songpagesoup=BeautifulSoup(songpage, "lxml")
    comments=getcommentssoup(songpagesoup)
    print(comments)
    
    
    
#    for j in range(2,30):        
#        payload = {'command': 'loadComments', 'sortable': 'DESC', 'orderby': 'ts_date', 'commenttypes':'all', 'page':str(j), 'specific_com': 'undefined'} # 'key2': 'value2' and so on (comma delimited)
#        r = requests.post('http:'+songpageadress, data=payload)
#        type(r)
#        if r.text == '<li>No Comments</li>':
#            print('no more comments')
#            break
#        else:
#            rtext=r.text
#            # Go one level deeper in the directory
#            k=open(songname+' commentspage '+str(j),'w',  encoding='utf-8')
#            rtext.encode('ascii', 'ignore')
#            k.write(rtext)
#            k.close()
#            print(rtext)


   
    
    
#soup.findAll('a', href=re.compile('^http://www.nhl.com/ice/boxscore.htm\?id='))
#print(type(dylanpagesoup))
#print(dylanpagesoup.prettify())
"""
XPATH of a song name
# XPATH - //*[@id="content-big"]/div/div[2]/div/table/tbody/tr[1]/td[1]/a
"""