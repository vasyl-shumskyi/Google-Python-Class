#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

#lst = []

#f = open(sys.argv[1], 'r')
#year = re.findall(r'<h3 align="center">Popularity in (\d+)', f.read())

#f = open(sys.argv[1], 'r')
#rank_names = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)', f.read())

#lst.append(year[0])
#
#for x in rank_names: 
#  lst.append(x[1] + ' ' + x[0])
#  lst.append(x[2] + ' ' + x[0]) 

#for y in sorted(lst): print y
   
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  lst = []
  dic = {}
#  out = ''

  f = open(filename, 'r')
  year = re.findall(r'Popularity in (\d+)', f.read())
  f.close()

  f = open(filename, 'r')
  rank_names = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)', f.read())
  f.close()

  for x in rank_names:
    if x[1] not in dic: dic[x[1]] = x[0]
    if x[2] not in dic: dic[x[2]] = x[0]
  
  lst.append(year[0])
  for k,v in dic.items(): lst.append(k+' '+v)

#  for y in sorted(lst): out = out + y + '\n'
  out = '\n'.join(lst) 					#### MUCH BETTER 
  return out


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  for fname in args:
    text = extract_names(fname) 
    if not summary: print text
    else:
      sfile = fname + '.summary'
      f = open(sfile, 'w')
      f.write(text)
      f.close()
    

if __name__ == '__main__':
  main()
