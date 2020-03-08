teams = []
n = int(input())
maxCal = (0, 0)
res = 0
for _ in range(n):
    teams.append(tuple(map(int, input().split())))
    if teams[-1][0] > maxCal[0]: maxCal = teams[-1]
for team in teams:
    if team[1] >= maxCal[0]:
        res += 1
print(res)