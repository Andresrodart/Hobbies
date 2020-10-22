n = int(input())
a = list(map(int, input().rstrip().split()))
res = sum_ = 0
mod = 10 ** 9 + 7
for num in a:
	sum_ = (sum_ + num % mod) % mod
for num in a:
	sum_ -= num
	if sum_ < 0: sum_ += mod
	res += (((num % mod) * (sum_ % mod)) % mod)
	res %= mod
print(res)