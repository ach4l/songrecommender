# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:40:25 2017

@author: Fitec
"""
import re
from bs4 import BeautifulSoup
def getcommentssoup(songpagesoup):
    comments=songpagesoup.find_all("div", class_='text')
    #for comment in comments:
        
    
    
    
    
    return comments
    
    


# //*[@id="comment-73014810051"]