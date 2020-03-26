# HT = HastTable

def PalindromePermutation(string):			# Just for ascii strings
	string = string.lower().replace(' ', '')		# O(n)
	HT = {}									# O(1)
	impair = 0								# O(1)
	for char in string:						# O(n)
		if char in HT: HT[char] +=1				# O(1)
		else: HT[char] = 1						# O(1)
	for value in HT.values():					# O(n)
		if bool(value & 1): impair += 1
		if impair > 1: return False
	return True

print(PalindromePermutation('Hello world!'))
print(PalindromePermutation('Tact Coa'))
print(PalindromePermutation('carerac'))
print(PalindromePermutation('aa'))
print(PalindromePermutation('accba'))
print(PalindromePermutation('asccba'))