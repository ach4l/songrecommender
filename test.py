# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:43:56 2017

@author: Fitec
"""

import re

teststr='<strong class="title">General Comment</strong>I think  writing about chaos. The universe is in organized chaos and Dylan had to "rearrange their faces" to make sense of it all.'
p=re.compile('[<>]')
a=re.split(p,teststr)

print(a)