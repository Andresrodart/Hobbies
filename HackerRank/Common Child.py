def commonChild(s1, s2):
	cS1 = {}
	cS2 = {}
	s1_ = list(s1)
	s2_ = list(s2)
	s1 = []
	s2 = []
	res = 0
	for i in range(len(s1_)):
		if s1_[i] not in cS1:
			cS1[s1_[i]] = [i]
		if s2_[i] not in cS2:
			cS2[s2_[i]] = [i]
		if	s2_[i] == s1_[i]:
			s2_.pop(i)
			s1_.pop(i)
			res += 1

	for i in range(len(s1_)):
		if s1_[i] in cS2:
			s1.append(s1_[i])
		if s2_[i] in cS1:
			s2.append(s2_[i])

	LstComnSec = [[None] * (len(s2) + 1)  for i in range(len(s1) + 1)]	#We are going to save here all the subSecuencies que can find starring with 0, where is the initiali case
	for i in range(len(s1) + 1):										#We dont iterate directly from the string because we need to loo in our aux matrix
		for j in range(len(s2) + 1):
			if j == 0 or i == 0:
				LstComnSec[i][j] = 0
			elif s1[i - 1] == s2[j - 1]:
				LstComnSec[i][j] = 1 + LstComnSec[i - 1][j - 1]
			else:
				LstComnSec[i][j] =  max(LstComnSec[i][j - 1], LstComnSec[i - 1][j])
	return LstComnSec[len(s1)][len(s2)] + res


print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))

# def commonChild(s1, s2):
#     cS1 = {}
#     cS2 = {}
#     cR1 = []
#     cR2 = []
#     res_1, res_2, iAt = 0, 0, -1
#     for c_1, c_2, i in zip(s1, s2, range(len(s1))):
#         if c_1 not in cR1:
#             if c_2 == c_1:
#                 res_1 += 1
#                 cR1 = []
#             else: 
#                 cR1.append(c_2)
#         else:
#             sliceIndex = cR1.index(c_1)
#             cR1 = cR1[0:sliceIndex + 1]
#             res_1 += 1
        
#         if c_2 not in cR2:
#             if c_2 == c_1:
#                 res_2 += 1
#                 cR2 = []
#             else: 
#                 cR2.append(c_1)
#         else:
#             sliceIndex = cR2.index(c_2)
#             cR2 = cR2[0:sliceIndex + 1]
#             res_2 += 1

#     return res_1 if res_1 > res_2 else res_2