#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++

################### VARIANT #1 (fast) ############################
def dictionary(filename):

  x = 1
  dict = {}

  f = open(filename,'r')
  oneline =  f.read() 
  f.close()

  oneline = oneline.lower().split()

  for word in oneline: 
    if word not in dict: dict[word] = 1 
    else: dict[word] = dict[word] + 1 
  
  return dict


def print_words(filename):

  dict = dictionary(filename)
  words = sorted(dict.items())
  for k,v in words: print k,v



def print_top(filename):
  
  dict = dictionary(filename)
  def sort_value(x): return x[-1]
  words =  sorted(dict.items(), key=sort_value, reverse=True)
  for k,v in words[:20]: print k,v
###############################################


########### VARIANT #2 (slow) ########################
#x = 1
#dict = {}
#oneline = ''

#f = open(sys.argv[2],'r')
#for line in f: oneline = oneline + line
#f.close()

############ SLOW ############
#oneline = sorted(oneline.lower().split())

#while oneline:
#  word = oneline[0]
#  if len(oneline) > 1 and oneline[0] == oneline[1]:
#    x += 1
#    oneline.pop(0)
#  else:
#    dict[word] = x
#    x = 1
#    oneline.pop(0)
##############################


#def print_words(filename):

#  words = sorted(dict.items())
#  for k,v in words: print k,v


#def print_top(filename):

#  def sort_value(x): return x[-1]
#    if len(dict) > 20:
#      for k in range(20): print words[k][0], words[k][1]
#    else:
#      for k, v in words: print k, v
###############################################


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]

  if option == '--count':
    print_words(filename)

  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
