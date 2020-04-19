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
def check_alphabet(passwords, loginAttempt):
	letters = set(loginAttempt)
	password = set(''.join(passwords))
	for char in letters:
		if char not in password: return False
	return True
	
def passwordCracker(passwords, loginAttempt):
	i, res, backtracking = 0, [], {}
	if not check_alphabet(passwords, loginAttempt): return 'WRONG PASSWORD'
	while i < len(loginAttempt):
		good = False
		start = 0 if i not in backtracking else backtracking[i]
		for index in range(start, len(passwords)):
			if passwords[index] == loginAttempt[i: i + len(passwords[index])]:
				good = True
				res.append(passwords[index])
				backtracking[i] = index + 1
				i += len(passwords[index])
				break
		if not res: return 'WRONG PASSWORD'
		if not good:
			i -= len(res.pop())
	return ' '.join(res)

if __name__ == '__main__':
	t = int(input().strip())
	result = ''
	for t_itr in range(t):
		n = int(input().strip())
		passwords = input().rstrip().split()
		loginAttempt = input()
		result += passwordCracker(passwords, loginAttempt) + '\n'
	print(result)