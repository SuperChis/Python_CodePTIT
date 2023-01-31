ans = 0
for t in range(int(input())):
    n = int(input())
    i = 2
    while i * i <= n:
        while n % i == 0:
            ans += i
            n //= i
        i += 1
    if n > 1: ans += n
print(ans)
