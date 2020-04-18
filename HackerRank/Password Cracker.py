#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#
def isInside(smaller, bigger):
	index = bigger.find(smaller)
	if index == -1:
		return([(bigger, False)])

	res, prev, mid, post = [], [], [], []
	for i in range(index): prev.append(bigger[i])
	for i in range(index + len(smaller), len(bigger)): post.append(bigger[i])
	if len(prev) != 0: res.append((''.join(prev), False))
	res.append((smaller, True))
	if len(post) != 0: res.append((''.join(post), False))
	return(res)

def passwordCracker(passwords, loginAttempt):
	passwords.sort(key = len, reverse = True)
	tokenizer, res = [(loginAttempt, False)], []
	for password in passwords:
		aux = []
		for token in tokenizer:
			if not token[1] and len(password) <= len(token[0]): aux.extend(isInside(password, token[0]))
			else: aux.append(token)
		tokenizer = [item for item in aux]
		print(tokenizer)
	
	for token in tokenizer:
		if not token[1]: return 'WRONG PASSWORD'
		res.append(token[0] + ' ')
	return ''.join(res)

if __name__ == '__main__':
	t = int(input().strip())
	result = ''
	for t_itr in range(t):
		n = int(input().strip())
		passwords = input().rstrip().split()
		loginAttempt = input()
		result += passwordCracker(passwords, loginAttempt) + ''
	print(result)
