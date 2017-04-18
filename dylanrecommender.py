# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:15:18 2017

@author: Fitec
"""

import nltk
import urllib
import re as regexp

dylanpage=urllib.request.urlopen('http://songmeanings.com/query/?query=bob%20dylan&type=songtitles')
dylanpagehtml = dylanpage.read()
#print(dylanpagehtml)
b'<td width="70%" class="marked">' in dylanpagehtml

alpha='<a style class href="'
beta='" title'
dylanpagetext=dylanpagehtml.decode('utf-8')
f=open('pagetext','w')
f.write(dylanpagetext)
f.close()
g=open('pagetext','w')
for line in g.readlines()
#ax=dylanpagetext.split(alpha)[-1].split(beta)[0]
#print(ax)
#f = open('myfile', 'w')
#f.write('hi there\n')  # python will convert \n to os.linesep
#f.close()


