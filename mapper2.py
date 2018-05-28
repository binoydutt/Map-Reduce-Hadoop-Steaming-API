#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 23:50:55 2017

@author: binoy
"""
import sys
sys.path.append('./')
from stopwords import *
import sys
import re

if __name__ =='__main__':
    filename =''    
    for line in sys.stdin:
        lst = line.split(':::')
        for author in lst[1].split('::'):
            lst[2] = lst[2].replace('-','')        
            regex = r'\w+'
            words = re.findall(regex,lst[2])
            for word in words:
                if word not in allStopWords and len(word)>1:
                    sys.stdout.write('{0}\t{1}\n'.format(author, word.lower()))
    
