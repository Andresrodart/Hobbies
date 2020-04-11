# Code adapted in python 3 from ecnerwala submission
T = int(input())
# O(NM)
def look_for_pref_mid_and_suf(list_of_strings, number_of_string):
	pref, mid, suff = [], [], []
	for i in range(number_of_string):
		# get the first and last appearance of an asterisk
		first_asterisk = list_of_strings[i].index('*')
		last__asterisk = len(list_of_strings[i]) - 1 - list_of_strings[i][::-1].index('*')
		# Check if the prefix of the current string is the same as the previous
		z = 0 # Note that at first pref is empty
		while z < len(pref) and z < first_asterisk:
			if pref[z] != list_of_strings[i][z]: return '*'
			z += 1
		# If the new string has a more restrictive prefix, we add the elements to the prefix list
		z = len(pref) # Note that previous elements are the same so we just need to add the new ones after actual prefix
		while z < first_asterisk: 
			pref.append(list_of_strings[i][z])
			z += 1
		# Same for the suffix, check if the suffix is equal
		z = 0 # Note that suffix reversed to simplified the iteration i.e. compare the first element in suffix with the last of the string -> 0 with len(string) - 1, 1 with len(...) - 2, ..., len(suffix) with len(suffix) - len(...) -  1   
		while z < len(suff) and len(list_of_strings[i]) - 1 - z > last__asterisk:
			if suff[z] != list_of_strings[i][len(list_of_strings[i]) - 1 - z]: return '*'
			z += 1
		# The same, if suffix is more restrictive update it
		z = len(suff)
		while len(list_of_strings[i]) - 1 - z > last__asterisk:
			suff.append(list_of_strings[i][len(list_of_strings[i]) - 1 - z])
			z += 1
		# Now note that mid elements can be put in the middle of the result as we want
		z = first_asterisk
		while z <= last__asterisk:
			if list_of_strings[i][z] != '*': mid.append(list_of_strings[i][z])
			z += 1
		# print('\t preffix', pref)
		# print('\t mid', mid)
		# print('\t suffix', suff)
	suff.reverse()
	return ''.join(pref + mid + suff)

for case in range(1, T + 1):
	N = int(input())
	patterns = []
	for _ in range(N): patterns.append(list(input()))
	print('Case #{}: {}'.format(case, look_for_pref_mid_and_suf(patterns, N)))