#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(9999)

def _abbreviation(a, b, i, j, memo):
  key = str(i) + '-' + str(j)
  if key in memo: return memo[key]
  while j < len(b) and i < len(a):
    if a[i] != b[j]: break
    j, i = j + 1, i + 1
  
  if j >= len(b):
    memo[key] = True
    while i < len(a):
      if a[i].isupper(): memo[key] = False
      i += 1
  elif i >= len(a): memo[key] = False
  elif a[i].upper() == b[j]: memo[key] = _abbreviation(a, b, i + 1, j + 1, memo) or _abbreviation(a, b, i + 1, j, memo)
  elif a[i].isupper(): memo[key] = False 
  else: memo[key] = _abbreviation(a, b, i + 1, j, memo)
  
  return memo[key]

def abbreviation(a, b, q_itr):
  if len(b) > len(a): return 'NO'
  if not canFormString(a, b): return 'NO'
  memo = {}
  res = 'YES' if _abbreviation(a, b, 0, 0, memo) else 'NO'
  # print(memo)
  return res

def canFormString(a, b):
  i, j = 0, 0
  while j < len(b) and i < len(a):
    if a[i] == b[j] or a[i].capitalize() == b[j]: j, i = j + 1, i + 1
    else: i += 1
  return True if j >= len(b) else False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b, q_itr)

        fptr.write(result + '\n')

    fptr.close()
