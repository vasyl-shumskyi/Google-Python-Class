#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

#import urlparse

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  lst1 = []
  lst2 = []

  f = open(filename, 'rU')
  baseurl = re.search(r'(\S+)_(\S+)', filename)
  url = 'http://' + baseurl.group(2)

  for line in f:
    match = re.search(r'\S+puzzle\S+', line)
    if match:
      uri = match.group()   
      fullurl = url + uri  
      match2 = re.search(r'-\w+-\w+.jpg', uri)
      if match2 and fullurl not in lst2: lst2.append(fullurl)
      if not match2 and fullurl not in lst1: lst1.append(fullurl)
          
  f.close()
   
  if lst1: return sorted(lst1)
  if lst2: return sorted(lst2, key=Descramble)


def Descramble(url):
  tolist = url.split('-')
  return tolist[-1]

# ------- WORKING --------
#def Descramble(url):
#  tolist = url.split('-')
#  last = tolist[-1]
#  i = url.find(last)
#  return url[i:]

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  n = 0
  img_name = ''
  index = os.path.join(dest_dir, 'index.html')
  html = '<verbatim><html><body>\n'

  if not os.path.exists(dest_dir): os.mkdir(dest_dir)

  for url in img_urls:
    img_name = 'img' + str(n) 
    path = os.path.join(dest_dir, img_name)
    print 'Retrieving  :: ', url, '-->', dest_dir + '/' + img_name, '\n',
    urllib.urlretrieve(url, path)
    html = html + '<img src="' + img_name + '">'
    n += 1

  html = html + '\n</body></html>\n'
  print 'Creating    :: ', index, '\n',
  f = open(index, 'w')
  f.write(html)
  f.close()
 
  return

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
