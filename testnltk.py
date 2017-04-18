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
'<td width="70%" class="marked">' in dylanpage

