# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:11:03 2017

@author: Fitec
"""

import urllib
import nltk
import re
import requests

#x here is the text file containing comments on one page. To be used recursive
#y here is a str the filename where all the comments would be aggregated
def getcomments(x,y):
    countmessage=0
    countreply=0
    fo=open(y,'w')
    for line in x:
        if '<strong class="title">' in line:
            teststr=line
            p=re.compile('[<>]')
            a=re.split(p,teststr)
            commenttype=a[2]
            
            if commenttype=='Song Meaning' or commenttype == 'My Interpretation' or commenttype == 'General Comment' or commenttype == 'Memory' or commenttype == 'My Opinion':
                fo.write('____________MESSAGE STARTS HERE_______________'+'\n')
                fo.write('Type of message : '+ commenttype)
                countmessage=1
            else:
                countmessage=0
        elif '<div class="text">' in line:
            countreply=1
            fo.write('______________REPLY TO MESSAGE____________'+'\n')
        elif '<div class="sign">' in line and countmessage==1:
            countmessage=0
            endofcommentmessage='____________MESSAGE ENDS HERE_____________'+'\n'
            fo.write(endofcommentmessage)
        elif '<div class="sign">' in line and countreply==1:
            countreply=0
            fo.write('___________END OF REPLY_____________'+ '\n')
        elif countreply==1:
            fo.write(line)
            fo.write('\n')
        elif countmessage==1:
            #fo.write(a[5])
            fo.write(line)
            fo.write('/n')
            
            
                               
                    
    fo.close()        
    fr=open(y,'r')    
    print(fr.readlines())
    fr.close()
    return               
    