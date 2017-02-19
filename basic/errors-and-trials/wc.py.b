#!/bin/python

import sys 

oneline = ''
x = 1
dict = {}

f = open(sys.argv[1], 'rU')
for line in f:  oneline = oneline + line
f.close()

oneline = sorted(oneline.split())

while oneline: 
  word = oneline[0] 
  if len(oneline) > 1 and oneline[0] == oneline[1]:
    x += 1
    oneline.pop(0)
  else:
    dict[word] = x 
    x = 1
    oneline.pop(0)

def sort_value(x): return x[-1]
words = sorted(dict.items(), key=sort_value, reverse=True)

for k, v in words: print v, '\t', k
