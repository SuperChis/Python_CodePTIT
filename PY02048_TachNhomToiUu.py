n, k = [int(i) for i in input().split()]
a = sorted(list(map(int, input().split())))
ans = 1
for i in range(1, n):
    if a[i] - a[i-1] > k:
        ans += 1
print(ans)
