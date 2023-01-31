def Check(a, b, n):
    for i in range(n):
        if(a[i] > b[i]):
            return False
    return True

for t in range(int(input())):
    n = int(input())
    a = [int(i)  for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    if Check(a, b, n):
        print("YES")
    else:
        print("NO")