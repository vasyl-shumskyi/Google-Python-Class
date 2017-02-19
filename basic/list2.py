#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

#def remove_adjacent(nums):
#  # +++your code here+++
#  new_list = []
#  y = 0
#  for x in nums:
#     if nums[x-1] != nums[x]: 
#        new_list.append(nums[y])
#        y=x
#  if nums and nums[-1] != new_list[-1]: new_list.append(nums[-1])
#  return new_list

#def remove_adjacent(nums):
 # +++your code here+++
## for n in nums:
# i=1
# for n in nums:
#  print 'n=',n, 'len(nums)',len(nums)
#  if nums[i-1]==nums[i] and i<len(nums):
#   print 'len=', len(nums),'i=',i
#   nums.pop(i)
#  else:
#   i=i+1
# return nums


#def remove_adjacent(nums):
#  # +++your code here+++
#  y=0
#  for x in range(len(nums)-2):
#     if nums[x-1] == nums[x]:
#       y=x
#       nums.pop(y)
#     else: y = x-1
#  return nums

#def remove_adjacent(nums):
  # +++your code here+++
#  x = 1 
#  print nums
#  while x < len(nums): 
#    if nums[x-1] == nums[x]:
#       nums.pop(x) 
#       print '==', nums
#    else: 
#      x=x+1
#      print '!=', nums
#  return nums

########################## LAST (working both / while and for)

def remove_adjacent(nums):
  # +++your code here+++
  x = 1
  while x < len(nums):
    if nums[x-1] == nums[x]: nums.pop(x)
    else: x += 1
  return nums


def remove_adjacent(nums):
 # +++your code here+++
## for n in nums:
 backup = nums[:]
 i=1
 for n in nums:
   if i < len(backup) and backup[i-1] == backup[i]: backup.pop(i)
   else: i=i+1
 return backup





# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++  
  new_list = []
  print '\n', list1, list2
  for x in range(len(list1)):
    for y in range(len(list2)):
      if list1[x] >= list2[y]:  
         new_list.insert(x, list2[y])  
         list2.pop(y)
      else: new_list.append(list2[y])
  print '\n', list1, list2
  return new_list

def linear_merge(list1, list2):
  x = 1

  if list1 > list2: 
     big = list1
     small = list2
     y = len(list1) 
  else: 
    big = list2
    small = list1
    y = len(list2) 

  print '\n', list1, list2
  while x < y:
    if big[x] >= small[0]: 
      big.insert(x,small[0]) 
      small.pop(0)
      x += 1 
      y = len(list1)
    else: x += 1
  print  list1, list2, '\n'
  return big

def linear_merge(list1, list2):
  x = 0
  cp_list1 = list1[:]
  sum_list = list1 + list2
  while x < len(cp_list1): 
    print x, list1, list2 
    if list1[x] < list2[0]: 
       list1.insert(x,list2[0])
       list2.pop(0)
       x = 0
    x+=1
  return list1
     
def linear_merge(list1, list2):

   list1_cp = list1[:]
   list2_cp = list2[:]
   L1 = range(len(list1))
   L2 = range(len(list2))

   print list1, list2
   for x in L1:
      for y in L2:
         print 'x', x, 'y', y
         if list2 and list2[y] <= list1[x]:
           list1.insert(x,list2[y])
#           list2.pop(y)
#           x = 0
   print list1, list2
   return list1

def linear_merge(list1, list2):
  # +++your code here+++
  x = 0
  y = 0
  while x < len(list1):
    while y < len(list2):
      if list2 and list2[y] <= list1[x]: 
        list1.insert(x,list2[y])
        list2.pop(y) 
        print list1,list2
  #  if nums[x-1] == nums[x]: nums.pop(x)
      else: 
       x += 1
       y += 1

  return list1




########################## LAST (working)

def linear_merge(list1, list2):
  x = 0
  while list2:
    if list1[x] > list2[0]:
      list1.insert(x,list2[0])
      list2.pop(0)
    else:
      if x == len(list1)-1: 
        list1.append(list2[0])
        list2.pop(0)
      else: x += 1  
  #  print x, list1,list2
  return list1



  


# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
