def Check(n):
    if len(str(n)) < 2: return False
    else:
        if n == int(str(n)[::-1]): return True
    return False
n, m = [int(i)  for i in input().split()]
a = [[]] * n
ans  = 0
for i in range(n):
    a[i] = [int(j)  for j in input().split()]
    for j in range(m):
        if(Check(a[i][j]) and a[i][j] > ans): ans = a[i][j]
if(ans == 0):
    print("NOT FOUND")
else: print(ans)
for i in range(n):
    for j in range(m):
        if(a[i][j] == ans):
            print("Vi tri [{}][{}]".format(i, j))
