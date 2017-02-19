#!/bin/python

import random
import sys

dic = {}
lst = []
i = 1
k = 0

f = open(sys.argv[1], 'rU')
text = f.read().split()
f.close()

dic[''] = [text[0]]
for x in text:
  if x not in dic: dic[x] = text[i:]
  i+=1

while len(lst) < 200:
  if k < len(dic)-2:
    lst.append(dic.keys()[k])
    lst.append(random.choice(dic.values()[k]))
    k+=1
  else:
    lst.append(random.choice(dic.values()[1]))
    k = 1
for x in lst: print x,
