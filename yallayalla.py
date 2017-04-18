import urllib2 as web
import re

#article directory is like a dictionary with each article and its corresponding links
def articledirectory():
topicfile=open('topiclist.txt','r')
topiclist=topicfile.readlines()
    