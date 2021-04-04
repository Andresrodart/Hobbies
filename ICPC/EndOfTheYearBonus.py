import sys
N, B = map(int, input().rstrip().split())
performance = []
result = [sys.maxsize] * N
performance = list(map(int, input().rstrip().split()))
iterators = list(set(performance))
iterators.sort()
levels = {}
for i in range(N):
    if performance[i] in levels: levels[performance[i]].append(i)
    else: levels[performance[i]] = [i]

for i in iterators:
    if i == 0: 
        for index in levels[i]: result[index] = 0
    else:
        for index in levels[i]:
            prev = result[N - 1] if index == 0 else result[index - 1]
            next_ = result[0] if index == N - 1 else result[index + 1]
            p_prev = performance[N - 1] if index == 0 else performance[index - 1]
            p_next = performance[0] if index == N - 1 else performance[index + 1]
            if(prev == sys.maxsize and next_ == sys.maxsize): result[index] = B
            elif((p_prev == performance[index] and p_next == performance[index]) and min(prev, next_) != sys.maxsize): result[index] = min(prev, next_)
            elif(p_prev == performance[index] and p_prev != sys.maxsize): result[index] = prev
            elif(p_next == performance[index] and p_next != sys.maxsize): result[index] = next_
            elif(prev == sys.maxsize): result[index] = ((next_ // B) + 1) * B
            elif(next_ == sys.maxsize): result[index] = ((prev // B) + 1) * B
            else: result[index] = ((max(prev, next_) // B) + 1) * B
print(' '.join(str(x) for x in result))