import bisect
import sys
def solve(p, q, s):
	res = 0
	used = set()
	for n in reversed(q):
		res = max(res, bs(n, s, p))
	return res
def bs(number, max_difficulty, p):
	l, r = 0, len(p) - 1
	pos = 0
	while l < r:
		mid = (l + r) // 2
		if p[mid] + number <= max_difficulty: 
			pos = mid
			l = mid + 1
		else: r = mid - 1
	if pos < 0 or pos > len(p) or p[pos] + number > max_difficulty: return sys.maxsize
	# print(p[pos], number)
	return abs(p.pop(pos) - number)

if __name__ == "__main__":
	p_arry = []
	q_arry = []
	disances = []
	disances_index = []
	solution = []
	q_count = {}
	p_count = {}
	res = 0
	n, p, q, s = map(int, input().rstrip().split())
	while p:
		num = int(input())
		bisect.insort_right(p_arry, num)
		p_count[num] = p_count.get(num, 0) + 1
		p -= 1
	while q:
		num = int(input())
		bisect.insort_right(q_arry, num)
		q_count[num] = q_count.get(num, 0) + 1
		q -= 1
	if len(p_arry) > len(q_arry): 
		q_arry, p_arry = p_arry, q_arry
		q_count, p_count = p_count, q_count
	for i in range(len(q_arry)):
		num = q_arry[i]
		pos_l = bisect.bisect_left(p_arry, num - 1)
		pos_r = bisect.bisect_right(p_arry, num - 1)
		pos = bisect.bisect_right(disances_index, abs(p_arry[pos_l] - num))
		disances_index.insert(pos, abs(p_arry[pos_l] - num))
		disances.insert(pos, (i, pos_l))
		if pos_l != pos_r:
			pos = bisect.bisect_right(disances_index, abs(p_arry[pos_r] - num))
			disances_index.insert(pos, abs(p_arry[pos_r] - num))
			disances.insert(pos, (i, pos_r))
	print(disances, q_count, p_count)
	for x, y in disances:
		print(q_arry[x], p_arry[y])
		if q_arry[x] + p_arry[y] <= s and q_count[q_arry[x]] > 0 and p_count[p_arry[y]] > 0: 
			res += 1
			q_count[q_arry[x]] -= 1
			p_count[p_arry[y]] -= 1
			bisect.insort_right(solution, abs(q_arry[x] - p_arry[y]))
		if res == n: break

	if len(solution) == n: print(solution[-1])
	else: print(-1)