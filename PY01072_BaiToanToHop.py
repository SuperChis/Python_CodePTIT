n, k = [int(i) for i in input().split()]
a = []
b = [0] * n
def Try(i):
    for j in range(b[i-1]+1,n-k+i+1):
        b[i] = j
        if i == k:
            for x in range(1, k+1):
                print(a[b[x]-1], end =' ')
            print()
        else: Try(i+1)
map = dict()
tmp = [int(i) for i in input().split()]
for i in tmp:
    if i in map:
        n -= 1
    else:
        a.append(i)
        map[i] = 1
a.sort()
Try(1)