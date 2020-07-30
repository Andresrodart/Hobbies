def isSubstring(s1, s2):
	s2 =  s2 + s2
	if s1 in s2: return True
	else: return False
print(isSubstring('waterbottle', 'erbottlewat'))
print(isSubstring('waterbottle', 'erbottlewa'))