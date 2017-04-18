# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:29:05 2017

@author: Fitec
"""


import nltk
import urllib
import re as regexp
import requests
import os

dylanpage=urllib.request.urlopen('http://songmeanings.com/query/?query=bob%20dylan&type=songtitles')
dylanpagehtml = dylanpage.read()
#print(dylanpagehtml)
b'<td width="70%" class="marked">' in dylanpagehtml

dylanpagetext=dylanpagehtml.decode('utf-8')
f=open('pagetext2','w')
f.write(dylanpagetext)
f.close()
g=open('pagetext2','r')
h=open('songnames','w')
for line in g.readlines():
    if '<a style="" class="" href=' in line:
        url=line.split('"')[5]
        songname=line.split('"')[7]        
        h.writelines(url+"                "+songname)
        h.writelines('\n')
g.close()    
h.close()
fo=open('songnames','r')
ln=fo.readlines()
for il  in ln:
    songpageadress=il.split("                ")[0]
    print(songpageadress)
    songname=il.split("                ")[-1]
    songname = songname.rstrip()
    print(songname)
    songpage=urllib.request.urlopen('http:'+songpageadress)
    songpagehtml=songpage.read()
    songpagetext=songpagehtml.decode('utf-8')
    i=open(songname+'pagetext','w')
    i.write(songpagetext)
    i.close()
    #for j in range(2,10,20,30):
    for j in range(2,30):        
        payload = {'command': 'loadComments', 'sortable': 'DESC', 'orderby': 'ts_date', 'commenttypes':'all', 'page':str(j), 'specific_com': 'undefined'} # 'key2': 'value2' and so on (comma delimited)
        r = requests.post('http:'+songpageadress, data=payload)
        type(r)
        if r.text == '<li>No Comments</li>':
            print('no more comments')
            break
        else:
            rtext=r.text
            k=open(songname+' commentspage '+str(j),'w',  encoding='utf-8')
            rtext.encode('ascii', 'ignore')
            k.write(rtext)
            k.close()
            print(rtext)
#            rtext=r.text
#            rtext=rtext.decode('utf-8')
#            k=open('commentspage'+str(j),'w')
#            k.write(rtext)
#            k.close()
        
    
fo.close()