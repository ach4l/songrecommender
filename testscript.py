# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:59:50 2017

@author: Fitec
"""
import re

teststr2='<strong class="title">General Comment</strong>Ok so this is my interpretation of the song, and feel free to correct or comment on it:  this isnt one love story, but an assembly of multiple ones with a different character in each stanza.  each stanza describes a unique kind of love, but generally outline all the beauty and longing of love, in ALL of its manuerisms, not just a man for a woman.  here is the breakdown<br />'
p=re.compile('[<>]')
a=re.split(p,teststr2)
print(a[2])