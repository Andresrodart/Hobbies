#!/bin/python3

import math
import os
import random
import re
import sys
import operator as op
from functools import reduce


prime = {1 : 0}

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def primes(n):
    if n - 1 in prime:
        if isPrime(n):
            prime[n] = prime[n - 1] + 1
        else:
            prime[n] = prime[n - 1]
        return prime[n]
    else:
        prime[n] = primes(n - 1) + (1 if isPrime(n) else 0)
        return prime[n]

# Complete the redJohn function below.
def redJohn(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1
    else:
        result = 0
        for i in range(int(n / 4) + 1):
            result = result + ncr(n - i*4 + 1, i)
        return primes(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
