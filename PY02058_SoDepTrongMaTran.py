n, m = [int(i)  for i in input().split()]
a = [[]] * 50
Max = -1
Min = 9999999
for i in range(n):
    a[i] = [int(j) for j in input().split()]
    Max = max(Max, max(a[i]))
    Min = min(Min, min(a[i]))
ans = Max - Min
ok, check = 0, 0
for i in range(n):
    for j in range(m):
        if(a[i][j] == ans):
            ok = 1
            if not check:
                print(ans)
                check = 1
            print("Vi tri [{}][{}]".format(i, j))
if not ok:
    print("NOT FOUND")