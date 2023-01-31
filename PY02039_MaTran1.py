n = int(input())
a = [[]] * n
sum1 = 0
sum2 = 0
for i in range(n):
    a[i] = [int(j) for j in input().split()]
    sum1 += sum(a[i][i+1:])
    sum2 += sum(a[i][:i])
k = int(input())
ans = abs(sum1 - sum2)
if ans <= k:
    print("YES")
else:
    print("NO")
print(ans)