import math
import os
import random
import re
import sys
import heapq 
from bisect import bisect 

# Complete the activityNotifications function below.
# def activityNotifications(expenditure, d):
# 	trailing, count, res = [], [0] * 201, 0
# 	if len(expenditure) < d: return res
# 	for _ in range(d):
# 		count[expenditure[0]] += 1
# 		trailing.append(expenditure.pop(0))
# 	while expenditure:
# 		sorted_ = countSort(trailing, count)
# 		if d % 2 == 0: res += 1 if expenditure[0] >= 2 * ((sorted_[d//2] + sorted_[d//2 - 1]) / 2) else 0
# 		else: res += 1 if expenditure[0] >= 2 * sorted_[d//2] else 0
# 		count[trailing.pop(0)] -= 1
# 		count[expenditure[0]] += 1
# 		trailing.append(expenditure.pop(0))
# return res
# def activityNotifications(expenditure, d):
# 	trailing, count, res, mid = [0] * d, [0] * 201, 0, 0
# 	cumulative = [0] * 201
# 	if len(expenditure) < d: return res
# 	for i in range(d):
# 		count[expenditure[i]] += 1
# 		trailing[i] = expenditure[i]
# 	for i in range(len(expenditure) - d):
# 		cumulative[0] = count[0]
# 		for j in range(1, 201): cumulative[j] = cumulative[j - 1] + count[j]
# 		if d % 2 == 0: 
# 			for j in range(201):
# 				if cumulative[j] >= d // 2 + 1:
# 					mid = j
# 					#print(j)
# 					break
# 			for j in range(201):
# 				if cumulative[j] >= d // 2 : 
# 					# sprint(j)
# 					mid += j
# 					break
# 		else: 
# 			for j in range(201):
# 				if cumulative[j] >= d // 2 + 1: 
# 					mid = 2 * j
# 					#print(j)
# 					break
# 		res += 1 if expenditure[i + d] >= mid else 0
# 		count[trailing.pop(0)] -= 1
# 		count[expenditure[i + d]] += 1
# 		trailing.append(expenditure[i + d])
# 	return res
# def activityNotifications(expenditure, d):
# 	trailing, sorted_, res = [], 0
# 	if len(expenditure) < d: return res
# 	for i in range(d): 
# 		pos = bisect(trailing, expenditure[0], 0, len(trailing))
# 		trailing.insert(pos, expenditure.pop(0))
# 	while expenditure:
# 		if d % 2 == 0: res += 1 if expenditure[0] >= trailing[d//2] + trailing[d//2 - 1] else 0
# 		else: res += 1 if expenditure[0] >= 2 * trailing[d//2] else 0
# 		print(trailing, expenditure[0])
# 		trailing [].
# 		pos = bisect(trailing, expenditure[0], 0, len(trailing))
# 		trailing.append(expenditure.pop(0))
# 	return res	
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activityNotifications([10, 20, 30, 40, 50], 3))