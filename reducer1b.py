#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 18:01:19 2017

@author: binoy
"""


import sys

from itertools import groupby
from operator import itemgetter

class Reducer:
	def __init__(self, stream, sep = '\t'):
		self.stream = stream
		self.sep = sep

	def emit(self, k, v):
		sys.stdout.write("{0}{1}{2}\n".format(k, self.sep, v))

	def reduce(self):
         for word,group in groupby(self,itemgetter(0)):
             dic ={}
             for item in group:
#                 files.add(item[1])
                 if item[1] in dic:
                     dic[item[1]]+=1
                 else:
                    dic[item[1]] =1
             self.emit(word, dic)


	def __iter__(self):
         for line in self.stream:
                 w,val =line.split(self.sep)
                 w =w.lower().strip()
                 val = val.strip('\n')
                 yield w,val

reducer = Reducer(sys.stdin)
reducer.reduce()

