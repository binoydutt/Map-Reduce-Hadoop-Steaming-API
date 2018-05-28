#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 17:49:05 2017

@author: binoy
"""

import sys
import re
import os 

if __name__ =='__main__':
    filename =''    
    for line in sys.stdin:
        line = line.replace('-','')        
        regex = r'\w+'
        lst = re.findall(regex,line)
        for word in lst:
             filename = os.getenv('map_input_file').split('/')[-1]
             if len(word)>1:
                 sys.stdout.write('{0}\t{1}\n'.format(word.lower(), filename))

